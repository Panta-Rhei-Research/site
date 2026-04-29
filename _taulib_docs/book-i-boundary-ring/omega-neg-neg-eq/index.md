---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_neg_neg_eq",
  "permalink": "/verify/taulib/docs/book-i-boundary-ring/omega-neg-neg-eq/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Ring`.",
  "declaration_id": "TauLib.BookI.Boundary.Ring::omega_neg_neg_eq",
  "declaration_slug": "omega-neg-neg-eq",
  "kind": "theorem",
  "name": "omega_neg_neg_eq",
  "module_name": "TauLib.BookI.Boundary.Ring",
  "module_url": "/verify/taulib/docs/book-i-boundary-ring/",
  "source_line_start": 214,
  "source_line_end": 225,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L214-L225",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L214-L225",
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
- Source path: [`TauLib/BookI/Boundary/Ring.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L214-L225)
- Source range: L214-L225
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Double negation is identity: neg(neg(n)) has the same components as n. -/
```

## Source Excerpt

```lean
theorem omega_neg_neg_eq (n d : TauIdx) :
    ∀ (i : Nat), i < d →
    (omega_neg_list ((primorial d - n % primorial d) % primorial d) d).getD i 0 =
    (mk_omega_tail n d).components.getD i 0 := by
  intro i hi
  rw [omega_neg_list_getD _ d i hi]
  rw [mk_omega_tail_getD n d i hi]
  unfold reduce
  have hidvd : primorial (i + 1) ∣ primorial d := primorial_dvd (show i + 1 ≤ d by omega)
  rw [mod_mod_of_dvd _ _ _ hidvd]
  rw [neg_mod_dvd n hidvd]
  exact double_neg_mod n (primorial (i + 1)) (primorial_pos (i + 1))
```
