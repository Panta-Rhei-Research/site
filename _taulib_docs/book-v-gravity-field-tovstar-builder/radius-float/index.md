---
{
  "projection_kind": "taulib_declaration",
  "title": "SphericalCarrier.radiusFloat",
  "permalink": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/radius-float/",
  "summary_short": "`def` declaration in `TauLib.BookV.GravityField.TOVStarBuilder`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVStarBuilder::SphericalCarrier.radiusFloat",
  "declaration_slug": "radius-float",
  "kind": "def",
  "name": "SphericalCarrier.radiusFloat",
  "module_name": "TauLib.BookV.GravityField.TOVStarBuilder",
  "module_url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/",
  "source_line_start": 83,
  "source_line_end": 84,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L83-L84",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TOVStarBuilder",
        "url": "/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L83-L84",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookV.GravityField.TOVStarBuilder](/corpus/taulib/docs/book-v-gravity-field-tovstar-builder/)
- Source path: [`TauLib/BookV/GravityField/TOVStarBuilder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L83-L84)
- Source range: L83-L84
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Radius as Float. -/
```

## Source Excerpt

```lean
def SphericalCarrier.radiusFloat (c : SphericalCarrier) : Float :=
  Float.ofNat c.radius_numer / Float.ofNat c.radius_denom
```
