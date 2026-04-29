---
{
  "projection_kind": "taulib_declaration",
  "title": "partition_growth_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/partition-growth-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.GoldbachDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.GoldbachDeep::partition_growth_check",
  "declaration_slug": "partition-growth-check",
  "kind": "def",
  "name": "partition_growth_check",
  "module_name": "TauLib.BookIII.Spectral.GoldbachDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/",
  "source_line_start": 98,
  "source_line_end": 108,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L98-L108",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L98-L108",
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
- Source path: [`TauLib/BookIII/Spectral/GoldbachDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L98-L108)
- Source range: L98-L108
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T70` — Partition Growth

## Immediate Comment / Docstring

```lean
/-- [III.T70] Partition growth check: r(M_{k+1}) > r(M_k). -/
```

## Source Excerpt

```lean
def partition_growth_check (lo hi : Nat) : Bool :=
  go lo (hi - lo + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k >= hi then true
    else
      let rk := goldbach_partition_count_at_primorial k
      let rk1 := goldbach_partition_count_at_primorial (k + 1)
      (rk1 > rk) && go (k + 1) (fuel - 1)
  termination_by fuel
```
