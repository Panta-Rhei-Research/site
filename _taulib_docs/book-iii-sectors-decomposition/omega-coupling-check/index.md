---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_coupling_check",
  "permalink": "/verify/taulib/docs/book-iii-sectors-decomposition/omega-coupling-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.Decomposition`.",
  "declaration_id": "TauLib.BookIII.Sectors.Decomposition::omega_coupling_check",
  "declaration_slug": "omega-coupling-check",
  "kind": "def",
  "name": "omega_coupling_check",
  "module_name": "TauLib.BookIII.Sectors.Decomposition",
  "module_url": "/verify/taulib/docs/book-iii-sectors-decomposition/",
  "source_line_start": 102,
  "source_line_end": 126,
  "registry_ids": [
    "III.D14",
    "III.T05"
  ],
  "related_registry_items": [
    {
      "id": "III.D14",
      "title": "ω-Coupling Sector",
      "url": "/registry/object/III.D14/"
    },
    {
      "id": "III.T05",
      "title": "Sector Preservation Theorem",
      "url": "/registry/object/III.T05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L102-L126",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.Decomposition",
        "url": "/verify/taulib/docs/book-iii-sectors-decomposition/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L102-L126",
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

- Module: [TauLib.BookIII.Sectors.Decomposition](/verify/taulib/docs/book-iii-sectors-decomposition/)
- Source path: [`TauLib/BookIII/Sectors/Decomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L102-L126)
- Source range: L102-L126
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D14` — ω-Coupling Sector
- `III.T05` — Sector Preservation Theorem

## Immediate Comment / Docstring

```lean
/-- [III.D14] ω-Coupling sector check: verify that ω-classified characters
    have both m ≠ 0 and n ≠ 0 (dual-lobe active) and |m| ≠ |n|.
    The ω-sector mediates coupling: it is the unique sector with
    both lobes active simultaneously. -/
```

## Source Excerpt

```lean
def omega_coupling_check (bound : TauIdx) : Bool :=
  go 0 0 ((bound + 1) * (bound + 1))
where
  go (m n fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if m > bound then true
    else if n > bound then go (m + 1) 0 (fuel - 1)
    else
      let χ : BoundaryCharacter := ⟨Int.ofNat m, Int.ofNat n⟩
      let ok := if sector_of χ == .Omega then
        -- ω-characters must have both indices nonzero and unequal magnitude
        m > 0 && n > 0 && m != n
      else true
      ok && go m (n + 1) (fuel - 1)
  termination_by fuel

-- ============================================================
-- SECTOR PRESERVATION THEOREM [III.T05]
-- ============================================================

/-! **Scope limitation (E3 collapse):** At finite primorial level, the E3
    predicate degenerates to E0 because `reduce` is idempotent. This check
    is vacuous but correctly models the mathematical structure. The E3 layer
    is correctly DEFINED but finite verification is vacuous.
    See audit DASHBOARD.md §E3 Collapse. -/
```
