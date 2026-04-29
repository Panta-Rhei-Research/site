---
{
  "projection_kind": "taulib_declaration",
  "title": "full_bndlift_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/full-bndlift-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.BndLift`.",
  "declaration_id": "TauLib.BookII.Hartogs.BndLift::full_bndlift_check",
  "declaration_slug": "full-bndlift-check",
  "kind": "def",
  "name": "full_bndlift_check",
  "module_name": "TauLib.BookII.Hartogs.BndLift",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/",
  "source_line_start": 359,
  "source_line_end": 380,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L359-L380",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.BndLift",
        "url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L359-L380",
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

- Module: [TauLib.BookII.Hartogs.BndLift](/verify/taulib/docs/book-ii-hartogs-bnd-lift/)
- Source path: [`TauLib/BookII/Hartogs/BndLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L359-L380)
- Source range: L359-L380
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.D36 + II.T26 + II.P08] Complete BndLift verification. -/
```

## Source Excerpt

```lean
def full_bndlift_check : Bool :=
  -- CRT structure
  crt_unique_check 1 &&
  crt_unique_check 2 &&
  crt_coverage_check 1 &&
  crt_coverage_check 2 &&
  -- Tower coherence
  bndlift_existence_check 3 30 &&
  tower_coherence_multi 3 30 &&
  lift_information_gain 4 &&
  -- CRT independence
  crt_independence_check 1 20 &&
  crt_independence_check 2 40 &&
  -- Channel independence
  bipolar_channel_independence 30 &&
  channel_decoupling_check 1 20 &&
  lift_sector_preservation 2 30 &&
  -- Extension structure
  extension_determinacy_check 1 &&
  extension_determinacy_check 2 &&
  splitting_count_check 1 &&
  splitting_count_check 2
```
