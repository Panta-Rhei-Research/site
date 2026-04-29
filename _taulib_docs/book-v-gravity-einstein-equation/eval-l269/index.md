---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L269",
  "permalink": "/verify/taulib/docs/book-v-gravity-einstein-equation/eval-l269/",
  "summary_short": "`eval` declaration in `TauLib.BookV.Gravity.EinsteinEquation`.",
  "declaration_id": "TauLib.BookV.Gravity.EinsteinEquation::#eval:269",
  "declaration_slug": "eval-l269",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.Gravity.EinsteinEquation",
  "module_url": "/verify/taulib/docs/book-v-gravity-einstein-equation/",
  "source_line_start": 269,
  "source_line_end": 272,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L269-L272",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.EinsteinEquation",
        "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L269-L272",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.BookV.Gravity.EinsteinEquation](/verify/taulib/docs/book-v-gravity-einstein-equation/)
- Source path: [`TauLib/BookV/Gravity/EinsteinEquation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L269-L272)
- Source range: L269-L272
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Example matter character
```

## Source Excerpt

```lean
#eval (MatterCharacter.mk 100 200 150 1000 (by omega)).totalFloat
  -- 0.45 (sum of three sectors)

end Tau.BookV.Gravity
```
