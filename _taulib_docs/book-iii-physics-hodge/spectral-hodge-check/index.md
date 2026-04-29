---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_hodge_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-hodge/spectral-hodge-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.Hodge`.",
  "declaration_id": "TauLib.BookIII.Physics.Hodge::spectral_hodge_check",
  "declaration_slug": "spectral-hodge-check",
  "kind": "def",
  "name": "spectral_hodge_check",
  "module_name": "TauLib.BookIII.Physics.Hodge",
  "module_url": "/verify/taulib/docs/book-iii-physics-hodge/",
  "source_line_start": 214,
  "source_line_end": 233,
  "registry_ids": [
    "III.P20"
  ],
  "related_registry_items": [
    {
      "id": "III.P20",
      "title": "Sector-by-Sector Protocol",
      "url": "/registry/object/III.P20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L214-L233",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.Hodge",
        "url": "/verify/taulib/docs/book-iii-physics-hodge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L214-L233",
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

- Module: [TauLib.BookIII.Physics.Hodge](/verify/taulib/docs/book-iii-physics-hodge/)
- Source path: [`TauLib/BookIII/Physics/Hodge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L214-L233)
- Source range: L214-L233
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P20` — Sector-by-Sector Protocol

## Immediate Comment / Docstring

```lean
/-- [III.P20] Spectral-Hodge compatibility: the Hodge filtration is
    compatible with the label-based spectral decomposition.
    B-filtration step ↔ B-type primes, C-step ↔ C-type primes. -/
```

## Source Excerpt

```lean
def spectral_hodge_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      -- B-sector product comes from B-type primes
      let bp := split_zeta_b k
      -- C-sector product comes from C-type primes
      let cp := split_zeta_c k
      -- X-sector product comes from X-type primes
      let xp := split_zeta_x k
      let pk := primorial k
      -- Compatibility: B*C*X = Prim(k) (spectral = Hodge)
      let compatible := if pk > 0 then bp * cp * xp == pk else true
      -- B and C coprime (filtration steps are orthogonal)
      let ortho := Nat.gcd bp cp == 1
      compatible && ortho && go (k + 1) (fuel - 1)
  termination_by fuel
```
