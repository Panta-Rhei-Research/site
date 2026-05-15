---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_yp",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/tau-yp/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.ThresholdLadder`.",
  "declaration_id": "TauLib.BookV.Cosmology.ThresholdLadder::tau_yp",
  "declaration_slug": "tau-yp",
  "kind": "def",
  "name": "tau_yp",
  "module_name": "TauLib.BookV.Cosmology.ThresholdLadder",
  "module_url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/",
  "source_line_start": 236,
  "source_line_end": 238,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L236-L238",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.ThresholdLadder",
        "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L236-L238",
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

- Module: [TauLib.BookV.Cosmology.ThresholdLadder](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/)
- Source path: [`TauLib/BookV/Cosmology/ThresholdLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L236-L238)
- Source range: L236-L238
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The τ-predicted He-4 mass fraction (Y_p = 20/81, floor(246.913) = 246). -/
```

## Source Excerpt

```lean
def tau_yp : NucleosynthesisResult where
  yp_times_1000 := 246
  consistent := ⟨by omega, by omega⟩
```
