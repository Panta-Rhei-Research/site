---
{
  "projection_kind": "taulib_declaration",
  "title": "classical_ns_as_readout",
  "permalink": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/classical-ns-as-readout/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.NavierStokesMacro`.",
  "declaration_id": "TauLib.BookV.FluidMacro.NavierStokesMacro::classical_ns_as_readout",
  "declaration_slug": "classical-ns-as-readout",
  "kind": "theorem",
  "name": "classical_ns_as_readout",
  "module_name": "TauLib.BookV.FluidMacro.NavierStokesMacro",
  "module_url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/",
  "source_line_start": 282,
  "source_line_end": 284,
  "registry_ids": [
    "V.P43"
  ],
  "related_registry_items": [
    {
      "id": "V.P43",
      "title": "Classical NS as readout",
      "url": "/registry/object/V.P43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L282-L284",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.NavierStokesMacro",
        "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L282-L284",
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

- Module: [TauLib.BookV.FluidMacro.NavierStokesMacro](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/)
- Source path: [`TauLib/BookV/FluidMacro/NavierStokesMacro.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L282-L284)
- Source range: L282-L284
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `V.P43` — Classical NS as readout

## Immediate Comment / Docstring

```lean
/-- [V.P43] Classical NS as readout: the classical incompressible
    Navier-Stokes equation on a chart domain U ⊂ ℝ³ is the
    readout-functor image of the macro tau-NS equation on the
    corresponding region of τ³, inheriting regularity on every
    compactly contained chart domain.

    Structural recording. -/
```

## Source Excerpt

```lean
theorem classical_ns_as_readout :
    "classical NS on U ⊂ ℝ³ = readout of macro tau-NS on τ³" =
    "classical NS on U ⊂ ℝ³ = readout of macro tau-NS on τ³" := rfl
```
