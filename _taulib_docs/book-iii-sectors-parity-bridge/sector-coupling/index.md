---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_coupling",
  "permalink": "/verify/taulib/docs/book-iii-sectors-parity-bridge/sector-coupling/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.ParityBridge`.",
  "declaration_id": "TauLib.BookIII.Sectors.ParityBridge::sector_coupling",
  "declaration_slug": "sector-coupling",
  "kind": "def",
  "name": "sector_coupling",
  "module_name": "TauLib.BookIII.Sectors.ParityBridge",
  "module_url": "/verify/taulib/docs/book-iii-sectors-parity-bridge/",
  "source_line_start": 64,
  "source_line_end": 84,
  "registry_ids": [
    "III.D18"
  ],
  "related_registry_items": [
    {
      "id": "III.D18",
      "title": "Coupling Ledger",
      "url": "/registry/object/III.D18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L64-L84",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.ParityBridge",
        "url": "/verify/taulib/docs/book-iii-sectors-parity-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L64-L84",
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

- Module: [TauLib.BookIII.Sectors.ParityBridge](/verify/taulib/docs/book-iii-sectors-parity-bridge/)
- Source path: [`TauLib/BookIII/Sectors/ParityBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L64-L84)
- Source range: L64-L84
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D18` — Coupling Ledger

## Immediate Comment / Docstring

```lean
/-- [III.D18] Compute the coupling between two sectors.
    κ(S_i, S_j) counts shared character-lattice structure:
    number of (m, n) pairs where sector_of(m,n) = S_i AND
    the character has non-trivial m-projection (if Sj is B-type)
    or n-projection (if Sj is C-type). -/
```

## Source Excerpt

```lean
def sector_coupling (si sj : Sector) (bound : TauIdx) : TauIdx :=
  go 0 0 0 ((bound + 1) * (bound + 1))
where
  go (m n acc fuel : Nat) : TauIdx :=
    if fuel = 0 then acc
    else if m > bound then acc
    else if n > bound then go (m + 1) 0 acc (fuel - 1)
    else
      let χ : BoundaryCharacter := ⟨Int.ofNat m, Int.ofNat n⟩
      let acc' := if sector_of χ == si then
        -- Does χ project non-trivially toward Sj?
        let projects := match sj with
          | .D => m == 0 && n == 0
          | .A => m == n
          | .B => m > 0
          | .C => n > 0
          | .Omega => m > 0 && n > 0 && m != n
        if projects then acc + 1 else acc
      else acc
      go m (n + 1) acc' (fuel - 1)
  termination_by fuel
```
