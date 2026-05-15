---
{
  "projection_kind": "taulib_declaration",
  "title": "goldbach_partition_count",
  "permalink": "/corpus/taulib/docs/book-iii-spectral-additive-conjectures/goldbach-partition-count/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.AdditiveConjectures`.",
  "declaration_id": "TauLib.BookIII.Spectral.AdditiveConjectures::goldbach_partition_count",
  "declaration_slug": "goldbach-partition-count",
  "kind": "def",
  "name": "goldbach_partition_count",
  "module_name": "TauLib.BookIII.Spectral.AdditiveConjectures",
  "module_url": "/corpus/taulib/docs/book-iii-spectral-additive-conjectures/",
  "source_line_start": 95,
  "source_line_end": 105,
  "registry_ids": [
    "III.D95"
  ],
  "related_registry_items": [
    {
      "id": "III.D95",
      "title": "Goldbach Representation",
      "url": "/registry/object/III.D95/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L95-L105",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.AdditiveConjectures",
        "url": "/corpus/taulib/docs/book-iii-spectral-additive-conjectures/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L95-L105",
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

- Module: [TauLib.BookIII.Spectral.AdditiveConjectures](/corpus/taulib/docs/book-iii-spectral-additive-conjectures/)
- Source path: [`TauLib/BookIII/Spectral/AdditiveConjectures.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L95-L105)
- Source range: L95-L105
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.D95` — Goldbach Representation

## Immediate Comment / Docstring

```lean
/-- [III.D95] Goldbach partition count: number of ways n = p + q
    with p ≤ q and both prime. -/
```

## Source Excerpt

```lean
def goldbach_partition_count (n : Nat) : Nat :=
  if n < 4 || n % 2 != 0 then 0
  else go 2 0 (n / 2 + 1)
where
  go (p acc fuel : Nat) : Nat :=
    if fuel = 0 then acc
    else if p > n / 2 then acc
    else
      let hit := if is_prime_nat p && is_prime_nat (n - p) then 1 else 0
      go (p + 1) (acc + hit) (fuel - 1)
  termination_by fuel
```
