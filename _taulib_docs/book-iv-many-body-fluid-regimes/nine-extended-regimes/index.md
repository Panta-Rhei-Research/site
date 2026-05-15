---
{
  "projection_kind": "taulib_declaration",
  "title": "nine_extended_regimes",
  "permalink": "/corpus/taulib/docs/book-iv-many-body-fluid-regimes/nine-extended-regimes/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.ManyBody.FluidRegimes`.",
  "declaration_id": "TauLib.BookIV.ManyBody.FluidRegimes::nine_extended_regimes",
  "declaration_slug": "nine-extended-regimes",
  "kind": "theorem",
  "name": "nine_extended_regimes",
  "module_name": "TauLib.BookIV.ManyBody.FluidRegimes",
  "module_url": "/corpus/taulib/docs/book-iv-many-body-fluid-regimes/",
  "source_line_start": 411,
  "source_line_end": 415,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L411-L415",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.FluidRegimes",
        "url": "/corpus/taulib/docs/book-iv-many-body-fluid-regimes/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L411-L415",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIV.ManyBody.FluidRegimes](/corpus/taulib/docs/book-iv-many-body-fluid-regimes/)
- Source path: [`TauLib/BookIV/ManyBody/FluidRegimes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L411-L415)
- Source range: L411-L415
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Total count of extended regimes. -/
```

## Source Excerpt

```lean
theorem nine_extended_regimes (r : ExtendedRegime) :
    r = .Crystal ∨ r = .Glass ∨ r = .Quasicrystal ∨ r = .Euler ∨
    r = .NavierStokes ∨ r = .MHD ∨ r = .Plasma ∨ r = .Superfluid ∨
    r = .Superconductor := by
  cases r <;> simp
```
