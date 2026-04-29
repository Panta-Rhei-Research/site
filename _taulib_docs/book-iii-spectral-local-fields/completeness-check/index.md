---
{
  "projection_kind": "taulib_declaration",
  "title": "completeness_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-local-fields/completeness-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.LocalFields`.",
  "declaration_id": "TauLib.BookIII.Spectral.LocalFields::completeness_check",
  "declaration_slug": "completeness-check",
  "kind": "def",
  "name": "completeness_check",
  "module_name": "TauLib.BookIII.Spectral.LocalFields",
  "module_url": "/verify/taulib/docs/book-iii-spectral-local-fields/",
  "source_line_start": 115,
  "source_line_end": 139,
  "registry_ids": [
    "III.P06"
  ],
  "related_registry_items": [
    {
      "id": "III.P06",
      "title": "Completeness Without Topology",
      "url": "/registry/object/III.P06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L115-L139",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.LocalFields",
        "url": "/verify/taulib/docs/book-iii-spectral-local-fields/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L115-L139",
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

- Module: [TauLib.BookIII.Spectral.LocalFields](/verify/taulib/docs/book-iii-spectral-local-fields/)
- Source path: [`TauLib/BookIII/Spectral/LocalFields.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L115-L139)
- Source range: L115-L139
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P06` — Completeness Without Topology

## Immediate Comment / Docstring

```lean
/-- [III.P06] Completeness check: every tower-coherent sequence has
    unique limit. A sequence (a_1, a_2, ...) with a_{n+1} ≡ a_n mod p^n
    determines a unique element of ℤ_p^τ.
    We verify: if we build a coherent tower from x, the limit = x mod p^d. -/
```

## Source Excerpt

```lean
def completeness_check (bound depth : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * 3)
where
  go (x p_idx fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if p_idx > 3 then go (x + 1) 1 (fuel - 1)
    else
      let p := nth_prime p_idx
      if p < 2 then go x (p_idx + 1) (fuel - 1)
      else
        -- Build coherent tower from x
        let tower_ok := check_tower x p 1 (depth + 1)
        tower_ok && go x (p_idx + 1) (fuel - 1)
  termination_by fuel
  check_tower (x p d fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if d > depth then true
    else
      let pd := p ^ d
      let pd1 := p ^ (d + 1)
      if pd == 0 || pd1 == 0 then true
      else
        (x % pd1) % pd == x % pd && check_tower x p (d + 1) (fuel - 1)
  termination_by fuel
```
