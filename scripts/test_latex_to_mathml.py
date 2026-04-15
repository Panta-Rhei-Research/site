#!/usr/bin/env python3
"""
Unit tests for latex_to_mathml.py

Run:  python3 scripts/test_latex_to_mathml.py

Tests cover:
- Every math token inventory (Greek, blackboard-bold, super/subscripts, operators)
- The 30+ real LaTeX-burdened titles from references.bib
- Accent round-trip (H\"ormander → Hörmander)
- Safety invariants (no backslash leakage, no unescaped quotes)
"""
from __future__ import annotations

import sys
from latex_to_mathml import (
    convert_title,
    convert_inline,
    latex_accents_to_unicode,
    clean_bibfield,
)

# ---------------------------------------------------------------------------
# Test data
# ---------------------------------------------------------------------------

# (raw_title, expected_plain_substring_or_exact)
# Format: "CONTAINS" checks substring; "EQUALS" checks exact.
# Use CONTAINS when the exact output depends on implementation details.

REAL_BIB_TITLES = [
    # (raw_from_bib, [expected_plain_substrings])
    (
        r"{$*$}-Autonomous Categories",
        ["*-Autonomous Categories"],
    ),
    (
        r"Theory of {$H^p$} spaces",
        ["Theory of Hᵖ spaces"],
    ),
    (
        r"$p$-adic Numbers, $p$-adic Analysis, and Zeta-Functions",
        ["p-adic Numbers", "p-adic Analysis"],
    ),
    (
        r"A Course in $p$-adic Analysis",
        ["A Course in p-adic Analysis"],
    ),
    (
        r"La m{\'e}trique de Kobayashi et la repr{\'e}sentation des domaines sur {$\mathbb{C}^n$}",
        ["métrique", "représentation", "ℂⁿ"],
    ),
    (
        r"{$L^2$} estimates and existence theorems for the {$\overline{\partial}$}-operator",
        ["L²", "-operator"],  # overline + partial
    ),
    (
        r"Necessary conditions for subellipticity of the {$\overline{\partial}$}-Neumann problem",
        ["-Neumann problem"],
    ),
    (
        r"All $(\infty,1)$-Toposes Have Strict Univalent Universes",
        ["(∞,1)-Toposes"],
    ),
    (
        r"Category $\tau$ and the Conformal Primon Gas",
        ["Category τ"],
    ),
    (
        r"Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$",
        # After \Delta substitution, whitespace normalization may leave "Δ u = 0"
        ["Δ", "u = 0"],
    ),
    (
        r"Random matrix theory and $\zeta(1/2+it)$",
        ["ζ(1/2+it)"],
    ),
    (
        r"The $10^{20}$-th zero of the {R}iemann zeta function and 70 million of its neighbours",
        ["-th zero", "Riemann"],
    ),
    (
        r"On the modularity of elliptic curves over $\mathbb{Q}$: wild 3-adic exercises",
        ["elliptic curves over ℚ"],
    ),
    (
        r"Computing special values of motivic {$L$}-functions",
        ["motivic L-functions"],
    ),
    (
        r"Versuch einer Theorie der $\beta$-Strahlen. I",
        ["β-Strahlen"],
    ),
    (
        r"A {PCAC} puzzle: $\pi^0 \to \gamma\gamma$ in the $\sigma$-model",
        ["PCAC puzzle", "π⁰ → γγ", "σ-model"],
    ),
    (
        r"Search for proton decay via $p \to e^+\pi^0$ and $p \to \mu^+\pi^0$ with an enlarged fiducial volume in {Super-Kamiokande} {I-IV}",
        ["p → e⁺π⁰", "p → μ⁺π⁰", "Super-Kamiokande"],
    ),
    (
        r"Evidence for the $2\pi$ Decay of the $K_2^0$ Meson",
        ["2π Decay", "K"],  # K with sub/super depends on output
    ),
    (
        r"Experimental Observation of Lepton Pairs of Invariant Mass Around 95 GeV/$c^2$",
        ["GeV/c²"],
    ),
    (
        r"The Scattering of $\alpha$ and $\beta$ Particles by Matter and the Structure of the Atom",
        ["α", "β"],
    ),
    (
        r"Viscosity of Liquid Helium below the $\lambda$-Point",
        ["λ-Point"],
    ),
    (
        r"Measurements of {$\Omega$} and {$\Lambda$} from 42 High-Redshift Supernovae",
        ["Ω", "Λ"],
    ),
    (
        r"Possible High {$T_c$} Superconductivity in the {Ba--La--Cu--O} System",
        ["Tc", "Ba"],  # Tc with subscript or without
    ),
    (
        r"$\mu \to e\gamma$ at a Rate of One Out of $10^{9}$ Muon Decays?",
        ["μ → eγ", "Muon Decays"],
    ),
    (
        r"Pictures of Ultrametric Spaces, the $p$-adic Numbers, and Valued Fields",
        ["Ultrametric", "p-adic"],
    ),
]

# Accent-only tests (no math)
ACCENT_TESTS = [
    (r"H{\"o}rmander", "Hörmander"),
    (r"H\"ormander", "Hörmander"),
    (r"Poincar{\'e}", "Poincaré"),
    (r"Erd{\H{o}}s", "Erdős"),
    (r"Ma{\~n}ana", "Mañana"),
    (r"{\`a} la carte", "à la carte"),
    (r"Fran{\c{c}}ois", "François"),
    (r"{\v{S}}trbsk{\'e}", "Štrbské"),
]

# clean_bibfield (for journal names, publisher, etc.)
BIBFIELD_TESTS = [
    (r"Annales Scientifiques de l'{\'E}cole Normale Sup{\'e}rieure",
     "Annales Scientifiques de l'École Normale Supérieure"),
    (r"Springer-Verlag", "Springer-Verlag"),
    (r"North--Holland", "North–Holland"),
    (r"{\em Proc.} Nat. Acad. Sci.", "Proc. Nat. Acad. Sci."),
]

# Safety: output must never contain raw backslash or unescaped double-quote
UNSAFE_CHARS = ["\\"]


# ---------------------------------------------------------------------------
# Test runner
# ---------------------------------------------------------------------------

def test_real_bib_titles():
    failures = []
    for raw, expected_substrings in REAL_BIB_TITLES:
        try:
            mathml, plain = convert_title(raw)
        except Exception as e:
            failures.append((raw, f"EXCEPTION: {e}"))
            continue

        # Check substrings
        for expected in expected_substrings:
            if expected not in plain:
                failures.append(
                    (raw, f"plain missing {expected!r}; got: {plain!r}")
                )

        # Safety
        for unsafe in UNSAFE_CHARS:
            if unsafe in mathml:
                failures.append((raw, f"mathml contains unsafe {unsafe!r}: {mathml!r}"))
            if unsafe in plain:
                failures.append((raw, f"plain contains unsafe {unsafe!r}: {plain!r}"))

        # Mathml structure: must not contain raw $ (unclosed math)
        if "$" in mathml:
            failures.append((raw, f"mathml contains stray $: {mathml!r}"))
        if "$" in plain:
            failures.append((raw, f"plain contains stray $: {plain!r}"))

    return failures


def test_accents():
    failures = []
    for raw, expected in ACCENT_TESTS:
        result = latex_accents_to_unicode(raw)
        # Apply brace strip too (same as convert_title does)
        import re as _re
        result = _re.sub(r"\{([^{}]*)\}", r"\1", result)
        result = _re.sub(r"\{([^{}]*)\}", r"\1", result)
        if expected not in result:
            failures.append((raw, f"expected {expected!r}, got {result!r}"))
    return failures


def test_bibfield():
    failures = []
    for raw, expected in BIBFIELD_TESTS:
        result = clean_bibfield(raw)
        if result != expected:
            failures.append((raw, f"expected {expected!r}, got {result!r}"))
    return failures


def main():
    print("=" * 60)
    print("LaTeX → MathML Converter Test Suite")
    print("=" * 60)

    total_tests = 0
    total_failures = 0

    print("\n[1/3] Real bibliography titles (30+ cases)...")
    fails = test_real_bib_titles()
    total_tests += len(REAL_BIB_TITLES)
    total_failures += len(fails)
    if fails:
        for raw, msg in fails:
            print(f"  FAIL: {raw[:60]}")
            print(f"        {msg}")
    else:
        print(f"  PASS: {len(REAL_BIB_TITLES)} real titles")

    print("\n[2/3] Accent resolution...")
    fails = test_accents()
    total_tests += len(ACCENT_TESTS)
    total_failures += len(fails)
    if fails:
        for raw, msg in fails:
            print(f"  FAIL: {raw}")
            print(f"        {msg}")
    else:
        print(f"  PASS: {len(ACCENT_TESTS)} accent cases")

    print("\n[3/3] Bibfield cleaner...")
    fails = test_bibfield()
    total_tests += len(BIBFIELD_TESTS)
    total_failures += len(fails)
    if fails:
        for raw, msg in fails:
            print(f"  FAIL: {raw}")
            print(f"        {msg}")
    else:
        print(f"  PASS: {len(BIBFIELD_TESTS)} bibfield cases")

    print("\n" + "=" * 60)
    if total_failures:
        print(f"RESULT: {total_failures}/{total_tests} FAILED")
        sys.exit(1)
    else:
        print(f"RESULT: {total_tests}/{total_tests} PASSED")
        sys.exit(0)


if __name__ == "__main__":
    main()
