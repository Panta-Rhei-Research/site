---
{
  "projection_kind": "taulib_declaration",
  "title": "goldbach_partition_count_at_primorial",
  "permalink": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/goldbach-partition-count-at-primorial/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.GoldbachDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.GoldbachDeep::goldbach_partition_count_at_primorial",
  "declaration_slug": "goldbach-partition-count-at-primorial",
  "kind": "def",
  "name": "goldbach_partition_count_at_primorial",
  "module_name": "TauLib.BookIII.Spectral.GoldbachDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/",
  "source_line_start": 92,
  "source_line_end": 95,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L92-L95",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L92-L95",
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

- Module: [TauLib.BookIII.Spectral.GoldbachDeep](/verify/taulib/docs/book-iii-spectral-goldbach-deep/)
- Source path: [`TauLib/BookIII/Spectral/GoldbachDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L92-L95)
- Source range: L92-L95
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D103` — Partition Count at Primorial

## Immediate Comment / Docstring

```lean
/-- [III.D103] Partition count at primorial level k. -/
```

## Source Excerpt

```lean
def goldbach_partition_count_at_primorial (k : Nat) : Nat :=
  let pk := primorial k
  let n := if pk >= 4 then (if pk % 2 == 0 then pk else pk - 1) else 4
  goldbach_partition_count_sieve n
```
