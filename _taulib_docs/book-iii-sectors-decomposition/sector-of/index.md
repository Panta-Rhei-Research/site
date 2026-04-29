---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_of",
  "permalink": "/verify/taulib/docs/book-iii-sectors-decomposition/sector-of/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.Decomposition`.",
  "declaration_id": "TauLib.BookIII.Sectors.Decomposition::sector_of",
  "declaration_slug": "sector-of",
  "kind": "def",
  "name": "sector_of",
  "module_name": "TauLib.BookIII.Sectors.Decomposition",
  "module_url": "/verify/taulib/docs/book-iii-sectors-decomposition/",
  "source_line_start": 55,
  "source_line_end": 63,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L55-L63",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L55-L63",
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
- Source path: [`TauLib/BookIII/Sectors/Decomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L55-L63)
- Source range: L55-L63
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D13` — 4+1 Sector Decomposition

## Immediate Comment / Docstring

```lean
/-- [III.D13] Sector assignment: classify a boundary character into its sector.
    Based on the dominance pattern of the (m, n) indices:
    - D: m = 0, n = 0 (trivial = radial)
    - A: |m| = |n|, both nonzero (balanced = weak)
    - B: |m| > |n| and n = 0 (pure B-lobe = electromagnetic)
    - C: |n| > |m| and m = 0 (pure C-lobe = strong)
    - Omega: both nonzero and |m| ≠ |n| (mixed coupling) -/
```

## Source Excerpt

```lean
def sector_of (χ : BoundaryCharacter) : Sector :=
  let am := χ.m_index.natAbs
  let an := χ.n_index.natAbs
  if am == 0 && an == 0 then .D
  else if am == an then .A
  else if am > an then
    if an == 0 then .B else .Omega
  else
    if am == 0 then .C else .Omega
```
