---
{
  "projection_kind": "taulib_declaration",
  "title": "c3_defect_contractivity",
  "permalink": "/corpus/taulib/docs/book-iv-many-body-fluid-regimes/c3-defect-contractivity/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.ManyBody.FluidRegimes`.",
  "declaration_id": "TauLib.BookIV.ManyBody.FluidRegimes::c3_defect_contractivity",
  "declaration_slug": "c3-defect-contractivity",
  "kind": "theorem",
  "name": "c3_defect_contractivity",
  "module_name": "TauLib.BookIV.ManyBody.FluidRegimes",
  "module_url": "/corpus/taulib/docs/book-iv-many-body-fluid-regimes/",
  "source_line_start": 477,
  "source_line_end": 481,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L477-L481",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L477-L481",
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
- Source path: [`TauLib/BookIV/ManyBody/FluidRegimes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L477-L481)
- Source range: L477-L481
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- C3 defect contractivity holds on T² fiber: λ₁₀ = 1, 2 cycles, 2 decay channels. -/
```

## Source Excerpt

```lean
theorem c3_defect_contractivity :
    defect_contractivity.first_eigenvalue = 1 ∧
    defect_contractivity.n_cycles = 2 ∧
    defect_contractivity.decay_channels = 2 :=
  ⟨rfl, rfl, rfl⟩
```
