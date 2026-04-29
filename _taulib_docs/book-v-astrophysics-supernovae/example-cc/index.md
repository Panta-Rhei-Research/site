---
{
  "projection_kind": "taulib_declaration",
  "title": "example_cc",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-supernovae/example-cc/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.Supernovae`.",
  "declaration_id": "TauLib.BookV.Astrophysics.Supernovae::example_cc",
  "declaration_slug": "example-cc",
  "kind": "def",
  "name": "example_cc",
  "module_name": "TauLib.BookV.Astrophysics.Supernovae",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-supernovae/",
  "source_line_start": 277,
  "source_line_end": 283,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L277-L283",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.Supernovae",
        "url": "/verify/taulib/docs/book-v-astrophysics-supernovae/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L277-L283",
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

- Module: [TauLib.BookV.Astrophysics.Supernovae](/verify/taulib/docs/book-v-astrophysics-supernovae/)
- Source path: [`TauLib/BookV/Astrophysics/Supernovae.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L277-L283)
- Source range: L277-L283
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Example: 20 M_☉ progenitor core collapse. -/
```

## Source Excerpt

```lean
def example_cc : CoreCollapseMechanism where
  progenitor_mass := 200  -- 20 M_☉
  massive_enough := by omega
  core_mass := 15         -- 1.5 M_☉ iron core
  exceeds_chandrasekhar := by native_decide
  remnant := .NeutronStar
  energy_released := 30   -- 3 × 10⁵¹ erg
```
