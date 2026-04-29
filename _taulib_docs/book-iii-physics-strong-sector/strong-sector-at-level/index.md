---
{
  "projection_kind": "taulib_declaration",
  "title": "strong_sector_at_level",
  "permalink": "/verify/taulib/docs/book-iii-physics-strong-sector/strong-sector-at-level/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.StrongSector`.",
  "declaration_id": "TauLib.BookIII.Physics.StrongSector::strong_sector_at_level",
  "declaration_slug": "strong-sector-at-level",
  "kind": "def",
  "name": "strong_sector_at_level",
  "module_name": "TauLib.BookIII.Physics.StrongSector",
  "module_url": "/verify/taulib/docs/book-iii-physics-strong-sector/",
  "source_line_start": 45,
  "source_line_end": 57,
  "registry_ids": [
    "III.D43"
  ],
  "related_registry_items": [
    {
      "id": "III.D43",
      "title": "Strong Sector at E₁",
      "url": "/registry/object/III.D43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L45-L57",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.StrongSector",
        "url": "/verify/taulib/docs/book-iii-physics-strong-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L45-L57",
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

- Module: [TauLib.BookIII.Physics.StrongSector](/verify/taulib/docs/book-iii-physics-strong-sector/)
- Source path: [`TauLib/BookIII/Physics/StrongSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L45-L57)
- Source range: L45-L57
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D43` — Strong Sector at E₁

## Immediate Comment / Docstring

```lean
/-- [III.D43] Strong sector check at level k: the B/C/X decomposition is
    unambiguous (coprimality), tower-stable (labels don't change with depth),
    and carries non-trivial content (B and C both have primes). -/
```

## Source Excerpt

```lean
def strong_sector_at_level (k : TauIdx) : Bool :=
  -- Coprimality: B-product and C-product are coprime
  let b_prod := split_zeta_b k
  let c_prod := split_zeta_c k
  let coprime := Nat.gcd b_prod c_prod == 1
  -- Non-triviality: both B and C sectors have primes (for k ≥ 3)
  let (b_ct, c_ct, _) := label_counts k
  let nontrivial := if k >= 3 then b_ct > 0 && c_ct > 0 else true
  -- Completeness: B * C * X = Prim(k)
  let x_prod := split_zeta_x k
  let pk := primorial k
  let complete := if pk > 0 then b_prod * c_prod * x_prod == pk else true
  coprime && nontrivial && complete
```
