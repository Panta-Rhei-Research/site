---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_neg_components_eq",
  "permalink": "/verify/taulib/docs/book-i-boundary-ring/omega-neg-components-eq/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Ring`.",
  "declaration_id": "TauLib.BookI.Boundary.Ring::omega_neg_components_eq",
  "declaration_slug": "omega-neg-components-eq",
  "kind": "theorem",
  "name": "omega_neg_components_eq",
  "module_name": "TauLib.BookI.Boundary.Ring",
  "module_url": "/verify/taulib/docs/book-i-boundary-ring/",
  "source_line_start": 164,
  "source_line_end": 176,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L164-L176",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L164-L176",
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
- Source path: [`TauLib/BookI/Boundary/Ring.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L164-L176)
- Source range: L164-L176
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Bridge: componentwise negation produces the negation representative at each stage. -/
```

## Source Excerpt

```lean
theorem omega_neg_components_eq (n d : TauIdx) :
    (mk_omega_tail_neg n d).components =
    (mk_omega_tail ((primorial d - n % primorial d) % primorial d) d).components := by
  have hlen : (mk_omega_tail_neg n d).components.length =
              (mk_omega_tail ((primorial d - n % primorial d) % primorial d) d).components.length :=
    (mk_omega_tail_neg n d).depth_eq.trans
      (mk_omega_tail ((primorial d - n % primorial d) % primorial d) d).depth_eq.symm
  apply List.ext_getElem hlen
  intro i h1 h2
  have hi : i < d := by rw [(mk_omega_tail_neg n d).depth_eq] at h1; exact h1
  rw [← getD_eq_getElem _ i 0 h1, ← getD_eq_getElem _ i 0 h2]
  show (omega_neg_list n d).getD i 0 = _
  rw [omega_neg_eq_reduce n d i hi, mk_omega_tail_getD _ d i hi]
```
