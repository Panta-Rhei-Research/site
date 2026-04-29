---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_preservation_check",
  "permalink": "/verify/taulib/docs/book-iii-sectors-decomposition/sector-preservation-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.Decomposition`.",
  "declaration_id": "TauLib.BookIII.Sectors.Decomposition::sector_preservation_check",
  "declaration_slug": "sector-preservation-check",
  "kind": "def",
  "name": "sector_preservation_check",
  "module_name": "TauLib.BookIII.Sectors.Decomposition",
  "module_url": "/verify/taulib/docs/book-iii-sectors-decomposition/",
  "source_line_start": 132,
  "source_line_end": 154,
  "registry_ids": [
    "III.T05"
  ],
  "related_registry_items": [
    {
      "id": "III.T05",
      "title": "Sector Preservation Theorem",
      "url": "/registry/object/III.T05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L132-L154",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L132-L154",
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
- Source path: [`TauLib/BookIII/Sectors/Decomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L132-L154)
- Source range: L132-L154
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T05` — Sector Preservation Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T05] Sector preservation check: verify that the BTI functor Φ
    preserves reduce-compatibility for each sector.
    For each character, the interior extension is reduce-stable:
    reduce(Φ(χ)(x, k), k) = Φ(χ)(x, k). -/
```

## Source Excerpt

```lean
def sector_preservation_check (bound db : TauIdx) : Bool :=
  go 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (m n k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if m > bound then true
    else if n > bound then go (m + 1) 0 1 (fuel - 1)
    else if k > db then go m (n + 1) 1 (fuel - 1)
    else
      let χ : BoundaryCharacter := ⟨Int.ofNat m, Int.ofNat n⟩
      -- BTI value is reduce-stable + tower-coherent
      let val := boundary_to_interior χ 1 k
      let stable := reduce val k == val
      -- Tower coherence: reduce at k then k-1 = reduce at k-1 directly
      -- (exercises Nat.mod_mod_of_dvd via primorial divisibility)
      let tower_ok := if k > 1 then
        let pk1 := primorial (k - 1)
        if pk1 > 0 then
          reduce val (k - 1) == reduce (reduce val k) (k - 1)
        else true
      else true
      stable && tower_ok && go m n (k + 1) (fuel - 1)
  termination_by fuel
```
