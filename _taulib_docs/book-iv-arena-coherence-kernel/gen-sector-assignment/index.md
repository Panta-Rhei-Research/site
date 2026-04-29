---
{
  "projection_kind": "taulib_declaration",
  "title": "GenSectorAssignment",
  "permalink": "/verify/taulib/docs/book-iv-arena-coherence-kernel/gen-sector-assignment/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Arena.CoherenceKernel`.",
  "declaration_id": "TauLib.BookIV.Arena.CoherenceKernel::GenSectorAssignment",
  "declaration_slug": "gen-sector-assignment",
  "kind": "def",
  "name": "GenSectorAssignment",
  "module_name": "TauLib.BookIV.Arena.CoherenceKernel",
  "module_url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/",
  "source_line_start": 39,
  "source_line_end": 45,
  "registry_ids": [
    "IV.D247"
  ],
  "related_registry_items": [
    {
      "id": "IV.D247",
      "title": "Generator--Sector Assignment",
      "url": "/registry/object/IV.D247/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L39-L45",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.CoherenceKernel",
        "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L39-L45",
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

- Module: [TauLib.BookIV.Arena.CoherenceKernel](/verify/taulib/docs/book-iv-arena-coherence-kernel/)
- Source path: [`TauLib/BookIV/Arena/CoherenceKernel.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L39-L45)
- Source range: L39-L45
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D247` — Generator--Sector Assignment

## Immediate Comment / Docstring

```lean
/-- [IV.D247] The bijective map Φ: {α,π,γ,η,ω} → {D,A,B,C,Ω}
    assigning each generator to its unique sector. -/
```

## Source Excerpt

```lean
def GenSectorAssignment (g : Generator) : Sector :=
  match g with
  | .alpha => .D
  | .pi    => .A
  | .gamma => .B
  | .eta   => .C
  | .omega => .Omega
```
