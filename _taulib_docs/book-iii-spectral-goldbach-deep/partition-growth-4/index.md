---
{
  "projection_kind": "taulib_declaration",
  "title": "partition_growth_4",
  "permalink": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/partition-growth-4/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.GoldbachDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.GoldbachDeep::partition_growth_4",
  "declaration_slug": "partition-growth-4",
  "kind": "theorem",
  "name": "partition_growth_4",
  "module_name": "TauLib.BookIII.Spectral.GoldbachDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/",
  "source_line_start": 182,
  "source_line_end": 183,
  "registry_ids": [
    "III.T70"
  ],
  "related_registry_items": [
    {
      "id": "III.T70",
      "title": "Partition Growth",
      "url": "/registry/object/III.T70/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L182-L183",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.GoldbachDeep",
        "url": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L182-L183",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookIII.Spectral.GoldbachDeep](/verify/taulib/docs/book-iii-spectral-goldbach-deep/)
- Source path: [`TauLib/BookIII/Spectral/GoldbachDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L182-L183)
- Source range: L182-L183
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T70` — Partition Growth

## Immediate Comment / Docstring

```lean
/-- [III.T70] Partition growth: r(M_k) increasing for k = 2..4. -/
```

## Source Excerpt

```lean
theorem partition_growth_4 :
    partition_growth_check 2 4 = true := by native_decide
```
