---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_add_components_eq",
  "permalink": "/verify/taulib/docs/book-i-polarity-omega-ring/omega-add-components-eq/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.OmegaRing`.",
  "declaration_id": "TauLib.BookI.Polarity.OmegaRing::omega_add_components_eq",
  "declaration_slug": "omega-add-components-eq",
  "kind": "theorem",
  "name": "omega_add_components_eq",
  "module_name": "TauLib.BookI.Polarity.OmegaRing",
  "module_url": "/verify/taulib/docs/book-i-polarity-omega-ring/",
  "source_line_start": 249,
  "source_line_end": 259,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaRing.lean#L249-L259",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.OmegaRing",
        "url": "/verify/taulib/docs/book-i-polarity-omega-ring/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaRing.lean#L249-L259",
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

- Module: [TauLib.BookI.Polarity.OmegaRing](/verify/taulib/docs/book-i-polarity-omega-ring/)
- Source path: [`TauLib/BookI/Polarity/OmegaRing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaRing.lean#L249-L259)
- Source range: L249-L259
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- mk_omega_tail_add produces the same components as mk_omega_tail of the sum.
    This is the master bridge: componentwise addition = global addition. -/
```

## Source Excerpt

```lean
theorem omega_add_components_eq (n1 n2 d : TauIdx) :
    (mk_omega_tail_add n1 n2 d).components = (mk_omega_tail (n1 + n2) d).components := by
  have hlen : (mk_omega_tail_add n1 n2 d).components.length =
              (mk_omega_tail (n1 + n2) d).components.length :=
    (mk_omega_tail_add n1 n2 d).depth_eq.trans (mk_omega_tail (n1 + n2) d).depth_eq.symm
  apply List.ext_getElem hlen
  intro i h1 h2
  have hi : i < d := by rw [(mk_omega_tail_add n1 n2 d).depth_eq] at h1; exact h1
  rw [← getD_eq_getElem _ i 0 h1, ← getD_eq_getElem _ i 0 h2]
  show (omega_add_list n1 n2 d).getD i 0 = (mk_omega_tail (n1 + n2) d).components.getD i 0
  rw [omega_add_eq_reduce n1 n2 d i hi, mk_omega_tail_getD (n1 + n2) d i hi]
```
