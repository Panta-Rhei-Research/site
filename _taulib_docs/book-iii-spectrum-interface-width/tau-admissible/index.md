---
{
  "projection_kind": "taulib_declaration",
  "title": "TauAdmissible",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-interface-width/tau-admissible/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectrum.InterfaceWidth`.",
  "declaration_id": "TauLib.BookIII.Spectrum.InterfaceWidth::TauAdmissible",
  "declaration_slug": "tau-admissible",
  "kind": "def",
  "name": "TauAdmissible",
  "module_name": "TauLib.BookIII.Spectrum.InterfaceWidth",
  "module_url": "/verify/taulib/docs/book-iii-spectrum-interface-width/",
  "source_line_start": 65,
  "source_line_end": 67,
  "registry_ids": [
    "I.D72"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L65-L67",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectrum.InterfaceWidth",
        "url": "/verify/taulib/docs/book-iii-spectrum-interface-width/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L65-L67",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookIII.Spectrum.InterfaceWidth](/verify/taulib/docs/book-iii-spectrum-interface-width/)
- Source path: [`TauLib/BookIII/Spectrum/InterfaceWidth.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L65-L67)
- Source range: L65-L67
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.D72] A StageFun is τ-admissible if there exists a uniform
    depth bound D such that for all inputs n, the function
    stabilizes at depth D.

    Equivalently: the function is completely determined by its
    action on ℤ/M_D ℤ for some finite D. -/
```

## Source Excerpt

```lean
def TauAdmissible (f : StageFun) : Prop :=
  ∃ D : TauIdx, ∀ n k : TauIdx, k ≤ D →
    reduce (f.b_fun n D) k = f.b_fun n k
```
