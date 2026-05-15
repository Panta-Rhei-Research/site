---
{
  "projection_kind": "taulib_declaration",
  "title": "partition_m4_pos",
  "permalink": "/corpus/taulib/docs/book-iii-spectral-goldbach-deep/partition-m4-pos/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.GoldbachDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.GoldbachDeep::partition_m4_pos",
  "declaration_slug": "partition-m4-pos",
  "kind": "theorem",
  "name": "partition_m4_pos",
  "module_name": "TauLib.BookIII.Spectral.GoldbachDeep",
  "module_url": "/corpus/taulib/docs/book-iii-spectral-goldbach-deep/",
  "source_line_start": 206,
  "source_line_end": 207,
  "registry_ids": [
    "III.D103"
  ],
  "related_registry_items": [
    {
      "id": "III.D103",
      "title": "Partition Count at Primorial",
      "url": "/registry/object/III.D103/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L206-L207",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.GoldbachDeep",
        "url": "/corpus/taulib/docs/book-iii-spectral-goldbach-deep/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L206-L207",
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

- Module: [TauLib.BookIII.Spectral.GoldbachDeep](/corpus/taulib/docs/book-iii-spectral-goldbach-deep/)
- Source path: [`TauLib/BookIII/Spectral/GoldbachDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L206-L207)
- Source range: L206-L207
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D103` — Partition Count at Primorial

## Immediate Comment / Docstring

```lean
/-- [III.D103] r(M_4) = r(210) > 0. -/
```

## Source Excerpt

```lean
theorem partition_m4_pos :
    goldbach_partition_count_at_primorial 4 > 0 := by native_decide
```
