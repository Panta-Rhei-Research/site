---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_decomposition_check",
  "permalink": "/verify/taulib/docs/book-iii-sectors-decomposition/sector-decomposition-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.Decomposition`.",
  "declaration_id": "TauLib.BookIII.Sectors.Decomposition::sector_decomposition_check",
  "declaration_slug": "sector-decomposition-check",
  "kind": "def",
  "name": "sector_decomposition_check",
  "module_name": "TauLib.BookIII.Sectors.Decomposition",
  "module_url": "/verify/taulib/docs/book-iii-sectors-decomposition/",
  "source_line_start": 75,
  "source_line_end": 92,
  "registry_ids": [
    "III.D13"
  ],
  "related_registry_items": [
    {
      "id": "III.D13",
      "title": "4+1 Sector Decomposition",
      "url": "/registry/object/III.D13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L75-L92",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L75-L92",
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
- Source path: [`TauLib/BookIII/Sectors/Decomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L75-L92)
- Source range: L75-L92
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D13` — 4+1 Sector Decomposition

## Immediate Comment / Docstring

```lean
/-- [III.D13] Sector decomposition check: verify that the 5 sectors
    are exhaustive over characters in range. Uses 5-bit accumulator. -/
```

## Source Excerpt

```lean
def sector_decomposition_check (bound : TauIdx) : Bool :=
  go 0 0 0 ((bound + 1) * (bound + 1))
where
  /-- Accumulate which sectors are seen. Bits: D=1, A=2, B=4, C=8, Omega=16. -/
  go (m n seen fuel : Nat) : Bool :=
    if fuel = 0 then seen == 31  -- 1+2+4+8+16 = 31
    else if m > bound then seen == 31
    else if n > bound then go (m + 1) 0 seen (fuel - 1)
    else
      let χ : BoundaryCharacter := ⟨Int.ofNat m, Int.ofNat n⟩
      let bit := match sector_of χ with
        | .D => 1
        | .A => 2
        | .B => 4
        | .C => 8
        | .Omega => 16
      go m (n + 1) (seen ||| bit) (fuel - 1)
  termination_by fuel
```
