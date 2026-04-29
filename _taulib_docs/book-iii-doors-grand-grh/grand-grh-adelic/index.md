---
{
  "projection_kind": "taulib_declaration",
  "title": "grand_grh_adelic",
  "permalink": "/verify/taulib/docs/book-iii-doors-grand-grh/grand-grh-adelic/",
  "summary_short": "`axiom` declaration in `TauLib.BookIII.Doors.GrandGRH`.",
  "declaration_id": "TauLib.BookIII.Doors.GrandGRH::grand_grh_adelic",
  "declaration_slug": "grand-grh-adelic",
  "kind": "axiom",
  "name": "grand_grh_adelic",
  "module_name": "TauLib.BookIII.Doors.GrandGRH",
  "module_url": "/verify/taulib/docs/book-iii-doors-grand-grh/",
  "source_line_start": 125,
  "source_line_end": 126,
  "registry_ids": [
    "III.D31"
  ],
  "related_registry_items": [
    {
      "id": "III.D31",
      "title": "Grand GRH (τ-effective)",
      "url": "/registry/object/III.D31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L125-L126",
  "formal_status": "axiom",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.GrandGRH",
        "url": "/verify/taulib/docs/book-iii-doors-grand-grh/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L125-L126",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "axiom",
      "status": "axiom"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookIII.Doors.GrandGRH](/verify/taulib/docs/book-iii-doors-grand-grh/)
- Source path: [`TauLib/BookIII/Doors/GrandGRH.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L125-L126)
- Source range: L125-L126
- Kind: `axiom`
- Formal status hint: `axiom`

## Registry Links

- `III.D31` — Grand GRH (τ-effective)

## Immediate Comment / Docstring

```lean
/-- [III.D31] **STATUS: OPEN CONJECTURE — all downstream results are CONDITIONAL ON GRH**

    This is a *named conditional hypothesis*, not a claim that TauLib proves the
    Generalized Riemann Hypothesis.  It exists solely so that `#print axioms`
    surfaces a legible token (`grand_grh_adelic`) on every downstream theorem
    that depends on GRH, making conditionality explicit and auditable.

    ---

    **What this axiom IS.**
    A crisp Lean 4 encoding of the assumption "the Grand Riemann Hypothesis holds
    in its adelic formulation" — the statement that, for every automorphic
    L-function attached to a reductive group over a global field, all non-trivial
    zeros lie on the critical line Re(s) = ½.  This is the same open conjecture
    treated as central in the Langlands program (Langlands 1970; Arthur 2002;
    Iwaniec–Sarnak 1999) and in analytic number theory (Montgomery–Vaughan 2006).
    It is listed as one of the Millennium Prize Problems (Clay Mathematics
    Institute, 2000) and remains unproved.

    **What this axiom is NOT.**
    It is NOT a claim that TauLib or the τ-framework proves GRH.  It is NOT
    evidence that GRH holds.  The finite `grand_grh_finite_check` passing
    `native_decide` at bounded primorial levels is a *consistency check* — it
    verifies that the framework's finite-level spectral decomposition (B/C/X
    sector purity, product completeness) is correct at those bounds.  Passing a
    finite check is a *necessary* condition for a framework compatible with GRH;
    it is *not sufficient* evidence for the universal adelic statement.  Do not
    read the `native_decide` theorems below as GRH evidence.

    **Conditional-result semantics.**
    Any TauLib theorem whose `#print axioms` output includes `grand_grh_adelic`
    is a conditional result.  It asserts: "IF the Grand Riemann Hypothesis holds
    (in adelic form) THEN [conclusion]."  The finite `grand_grh_finite_check`
    passing is a consistency check, not evidence for the universal statement.
    Readers should treat such theorems exactly as the classical literature treats
    theorems proved "assuming GRH."

    **Naming rationale.**
    The name `grand_grh_adelic` mirrors standard terminology: "Grand Riemann
    Hypothesis" (the automorphic generalization of GRH; cf. Sarnak's letter on
    the GRH, 2004) and "adelic" (the adèle-ring formulation central to the
    Langlands correspondence).  The name is intentionally descriptive so that
    `#print axioms` output is self-explanatory.  Do NOT rename this axiom
    without a coordinated downstream call-site update — the name is load-bearing
    for the `#print axioms` audit trail.

    **Paper cross-references.**
    - §7 (Custom Axioms): itemized discussion of this axiom alongside
      `bridge_functor_exists` and `spectral_correspondence_O3`; explains why
      global postulation was chosen over a hypothesis-threaded encoding.
    - §11 (Limitations): flags the hypothesis-refactor as explicit future work —
      replacing this global axiom with an explicit parameter
      `(h : GrandGRHAdelic)` on each downstream theorem, matching the
      Mathlib-community idiom for unproved conjectures.

    **Future refactor (planned, not present).**
    The Mathlib-community idiom is to thread such a conjecture as an explicit
    hypothesis `(h : GrandGRHAdelic)` on downstream theorems rather than
    postulate it globally.  The current global encoding was chosen for
    readability during the initial formalization wave.  The refactor is scoped
    to a future wave; see §11 Limitations. -/
```

## Source Excerpt

```lean
axiom grand_grh_adelic :
  ∀ k : Nat, grand_grh_finite_check k = true
```
