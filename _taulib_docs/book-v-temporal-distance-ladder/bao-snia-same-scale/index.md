---
{
  "projection_kind": "taulib_declaration",
  "title": "bao_snia_same_scale",
  "permalink": "/corpus/taulib/docs/book-v-temporal-distance-ladder/bao-snia-same-scale/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.DistanceLadder`.",
  "declaration_id": "TauLib.BookV.Temporal.DistanceLadder::bao_snia_same_scale",
  "declaration_slug": "bao-snia-same-scale",
  "kind": "theorem",
  "name": "bao_snia_same_scale",
  "module_name": "TauLib.BookV.Temporal.DistanceLadder",
  "module_url": "/corpus/taulib/docs/book-v-temporal-distance-ladder/",
  "source_line_start": 252,
  "source_line_end": 253,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L252-L253",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.DistanceLadder",
        "url": "/corpus/taulib/docs/book-v-temporal-distance-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L252-L253",
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

- Module: [TauLib.BookV.Temporal.DistanceLadder](/corpus/taulib/docs/book-v-temporal-distance-ladder/)
- Source path: [`TauLib/BookV/Temporal/DistanceLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L252-L253)
- Source range: L252-L253
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- BAO and SNIa operate at the same order of magnitude. -/
```

## Source Excerpt

```lean
theorem bao_snia_same_scale :
    DistanceLadderRung.BAO.log10_parsec = DistanceLadderRung.SNIa.log10_parsec := by rfl
```
