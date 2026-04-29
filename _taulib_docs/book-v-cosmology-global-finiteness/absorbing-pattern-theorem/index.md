---
{
  "projection_kind": "taulib_declaration",
  "title": "absorbing_pattern_theorem",
  "permalink": "/verify/taulib/docs/book-v-cosmology-global-finiteness/absorbing-pattern-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.GlobalFiniteness`.",
  "declaration_id": "TauLib.BookV.Cosmology.GlobalFiniteness::absorbing_pattern_theorem",
  "declaration_slug": "absorbing-pattern-theorem",
  "kind": "theorem",
  "name": "absorbing_pattern_theorem",
  "module_name": "TauLib.BookV.Cosmology.GlobalFiniteness",
  "module_url": "/verify/taulib/docs/book-v-cosmology-global-finiteness/",
  "source_line_start": 227,
  "source_line_end": 229,
  "registry_ids": [
    "V.T118"
  ],
  "related_registry_items": [
    {
      "id": "V.T118",
      "title": "Absorbing Pattern Theorem",
      "url": "/registry/object/V.T118/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L227-L229",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.GlobalFiniteness",
        "url": "/verify/taulib/docs/book-v-cosmology-global-finiteness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L227-L229",
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

- Module: [TauLib.BookV.Cosmology.GlobalFiniteness](/verify/taulib/docs/book-v-cosmology-global-finiteness/)
- Source path: [`TauLib/BookV/Cosmology/GlobalFiniteness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L227-L229)
- Source range: L227-L229
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T118` — Absorbing Pattern Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T118] Absorbing pattern theorem: the motif distribution on
    τ³ converges to a unique absorbing pattern P_∞ as refinement
    depth n → ∞.

    On the complement of BH excisions, P_∞ is the vacuum (minimal
    defect). Inside each excision, P_∞ is a single eternal BH motif.

    This negates "turtles all the way down": no infinite tower of
    ever-larger structures exists. -/
```

## Source Excerpt

```lean
theorem absorbing_pattern_theorem (ap : AbsorbingPattern)
    (hu : ap.is_unique = true) (hr : ap.rho_invariant = true) :
    ap.is_unique = true ∧ ap.rho_invariant = true := ⟨hu, hr⟩
```
