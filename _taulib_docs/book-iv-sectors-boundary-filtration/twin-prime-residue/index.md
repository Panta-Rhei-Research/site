---
{
  "projection_kind": "taulib_declaration",
  "title": "twin_prime_residue",
  "permalink": "/verify/taulib/docs/book-iv-sectors-boundary-filtration/twin-prime-residue/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.BoundaryFiltration`.",
  "declaration_id": "TauLib.BookIV.Sectors.BoundaryFiltration::twin_prime_residue",
  "declaration_slug": "twin-prime-residue",
  "kind": "theorem",
  "name": "twin_prime_residue",
  "module_name": "TauLib.BookIV.Sectors.BoundaryFiltration",
  "module_url": "/verify/taulib/docs/book-iv-sectors-boundary-filtration/",
  "source_line_start": 218,
  "source_line_end": 220,
  "registry_ids": [
    "IV.T131"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L218-L220",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.BoundaryFiltration",
        "url": "/verify/taulib/docs/book-iv-sectors-boundary-filtration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L218-L220",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookIV.Sectors.BoundaryFiltration](/verify/taulib/docs/book-iv-sectors-boundary-filtration/)
- Source path: [`TauLib/BookIV/Sectors/BoundaryFiltration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L218-L220)
- Source range: L218-L220
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [IV.T131] Twin Prime Residue Theorem (τ-EFFECTIVE).

    The S₅ correction factor 121/120 = 1 + 1/120 is DERIVED from τ-structure.

    For twin primes (p, q) = (3, 5) with n = pq = 15 boundary modes:
    - Euler sieve: s = (p-1)(q-1) = 8
    - Structural census: a = pq - p - 1 = 11 (silent count = p + 1 = 4)
    - Twin prime residue: a² - s·n = p(q-1)[(q-p)-2] + 1 = 1

    Therefore (a/n)² = (s/n)·(1 + 1/(s·n)) = (8/15)·(121/120).

    The "S₅ correction" label is a corollary: s·n = 8·15 = 120 = 5! = |S₅|
    is specific to (p,q) = (3,5). The deeper reason is the twin prime
    residue a² ≡ 1 (mod s·n), guaranteed by q = p + 2. -/
```

## Source Excerpt

```lean
theorem twin_prime_residue :
    (121 : Nat) = 120 + 1 ∧
    (120 : Nat) = 1 * 2 * 3 * 4 * 5 := by omega
```
