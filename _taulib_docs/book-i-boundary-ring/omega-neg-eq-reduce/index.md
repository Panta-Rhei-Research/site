---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_neg_eq_reduce",
  "permalink": "/verify/taulib/docs/book-i-boundary-ring/omega-neg-eq-reduce/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Ring`.",
  "declaration_id": "TauLib.BookI.Boundary.Ring::omega_neg_eq_reduce",
  "declaration_slug": "omega-neg-eq-reduce",
  "kind": "theorem",
  "name": "omega_neg_eq_reduce",
  "module_name": "TauLib.BookI.Boundary.Ring",
  "module_url": "/verify/taulib/docs/book-i-boundary-ring/",
  "source_line_start": 152,
  "source_line_end": 157,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L152-L157",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Ring",
        "url": "/verify/taulib/docs/book-i-boundary-ring/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L152-L157",
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

- Module: [TauLib.BookI.Boundary.Ring](/verify/taulib/docs/book-i-boundary-ring/)
- Source path: [`TauLib/BookI/Boundary/Ring.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L152-L157)
- Source range: L152-L157
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Negation reduces to standard negation: componentwise neg = global neg mod M_k. -/
```

## Source Excerpt

```lean
private theorem omega_neg_eq_reduce (n d i : Nat) (hi : i < d) :
    (omega_neg_list n d).getD i 0 = reduce ((primorial d - n % primorial d) % primorial d) (i + 1) := by
  rw [omega_neg_list_getD n d i hi]
  simp only [reduce]
  rw [mod_mod_of_dvd _ _ _ (primorial_dvd (show i + 1 ≤ d by omega))]
  exact (neg_mod_dvd n (primorial_dvd (show i + 1 ≤ d by omega))).symm
```
