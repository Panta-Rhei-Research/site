---
{
  "projection_kind": "taulib_declaration",
  "title": "mirror_master_check",
  "permalink": "/verify/taulib/docs/book-iii-mirror-saturation/mirror-master-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.Saturation`.",
  "declaration_id": "TauLib.BookIII.Mirror.Saturation::mirror_master_check",
  "declaration_slug": "mirror-master-check",
  "kind": "def",
  "name": "mirror_master_check",
  "module_name": "TauLib.BookIII.Mirror.Saturation",
  "module_url": "/verify/taulib/docs/book-iii-mirror-saturation/",
  "source_line_start": 181,
  "source_line_end": 197,
  "registry_ids": [
    "III.D73",
    "III.D74",
    "III.D75",
    "III.P31",
    "III.T48",
    "III.T49"
  ],
  "related_registry_items": [
    {
      "id": "III.D73",
      "title": "Proof Theory as E₃",
      "url": "/registry/object/III.D73/"
    },
    {
      "id": "III.D74",
      "title": "Diagrammatic Sector of E₃",
      "url": "/registry/object/III.D74/"
    },
    {
      "id": "III.D75",
      "title": "E₂→E₃ Boundary Crossing",
      "url": "/registry/object/III.D75/"
    },
    {
      "id": "III.P31",
      "title": "Terminal Level Characterization",
      "url": "/registry/object/III.P31/"
    },
    {
      "id": "III.T48",
      "title": "Four Paradox Diagnostic",
      "url": "/registry/object/III.T48/"
    },
    {
      "id": "III.T49",
      "title": "Applied Saturation",
      "url": "/registry/object/III.T49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L181-L197",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.Saturation",
        "url": "/verify/taulib/docs/book-iii-mirror-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L181-L197",
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

- Module: [TauLib.BookIII.Mirror.Saturation](/verify/taulib/docs/book-iii-mirror-saturation/)
- Source path: [`TauLib/BookIII/Mirror/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L181-L197)
- Source range: L181-L197
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D73` — Proof Theory as E₃
- `III.D74` — Diagrammatic Sector of E₃
- `III.D75` — E₂→E₃ Boundary Crossing
- `III.P31` — Terminal Level Characterization
- `III.T48` — Four Paradox Diagnostic
- `III.T49` — Applied Saturation

## Immediate Comment / Docstring

```lean
/-- Master mirror check: combines all Sprint 10 verifications.
    Proof theory (E3), self-model functor, paradox resolution,
    applied saturation, and terminal level characterization. -/
```

## Source Excerpt

```lean
def mirror_master_check (bound db : TauIdx) : Bool :=
  -- Proof theory as E3 [III.D73]
  proof_theory_e3_check bound db &&
  -- Self-model functor [III.D74]
  self_model_check bound db &&
  -- Four paradox diagnostic [III.D75]
  four_paradox_check bound db &&
  -- Paradox resolution [III.T48]
  paradox_resolution_check bound db &&
  -- Applied saturation [III.T49]
  applied_saturation_check bound db &&
  -- Terminal level [III.P31]
  terminal_level_check bound db &&
  -- Tower completeness
  tower_complete_check &&
  -- Reachability
  reachability_check
```
