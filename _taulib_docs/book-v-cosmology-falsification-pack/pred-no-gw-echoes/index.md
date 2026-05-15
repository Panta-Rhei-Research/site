---
{
  "projection_kind": "taulib_declaration",
  "title": "pred_no_gw_echoes",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/pred-no-gw-echoes/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.FalsificationPack`.",
  "declaration_id": "TauLib.BookV.Cosmology.FalsificationPack::pred_no_gw_echoes",
  "declaration_slug": "pred-no-gw-echoes",
  "kind": "def",
  "name": "pred_no_gw_echoes",
  "module_name": "TauLib.BookV.Cosmology.FalsificationPack",
  "module_url": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/",
  "source_line_start": 134,
  "source_line_end": 139,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L134-L139",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.FalsificationPack",
        "url": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L134-L139",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookV.Cosmology.FalsificationPack](/corpus/taulib/docs/book-v-cosmology-falsification-pack/)
- Source path: [`TauLib/BookV/Cosmology/FalsificationPack.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L134-L139)
- Source range: L134-L139
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- S4: No reflective-surface GW echoes.
    This structural no-echo claim is about exotic compact object
    reflective surfaces behind the horizon. It is distinct from the
    T² cycle-delay topology readouts in `BHTopoModes`. -/
```

## Source Excerpt

```lean
def pred_no_gw_echoes : TestablePrediction where
  name := "S4: No reflective-surface GW echoes"
  level := .Structural
  description := "No exotic reflective surface behind the horizon; T^2 cycle-delay readouts are a separate topology-readout prediction."
  status := "No reflective-surface echoes detected (consistent)"
  currently_testable := true
```
