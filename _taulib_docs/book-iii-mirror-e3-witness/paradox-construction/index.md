---
{
  "projection_kind": "taulib_declaration",
  "title": "paradox_construction",
  "permalink": "/verify/taulib/docs/book-iii-mirror-e3-witness/paradox-construction/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.E3Witness`.",
  "declaration_id": "TauLib.BookIII.Mirror.E3Witness::paradox_construction",
  "declaration_slug": "paradox-construction",
  "kind": "def",
  "name": "paradox_construction",
  "module_name": "TauLib.BookIII.Mirror.E3Witness",
  "module_url": "/verify/taulib/docs/book-iii-mirror-e3-witness/",
  "source_line_start": 115,
  "source_line_end": 122,
  "registry_ids": [
    "III.D86"
  ],
  "related_registry_items": [
    {
      "id": "III.D86",
      "title": "Paradox Absorption Map",
      "url": "/registry/object/III.D86/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L115-L122",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.E3Witness",
        "url": "/verify/taulib/docs/book-iii-mirror-e3-witness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L115-L122",
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

- Module: [TauLib.BookIII.Mirror.E3Witness](/verify/taulib/docs/book-iii-mirror-e3-witness/)
- Source path: [`TauLib/BookIII/Mirror/E3Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L115-L122)
- Source range: L115-L122
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D86` — Paradox Absorption Map

## Immediate Comment / Docstring

```lean
/-- [III.D86] Paradox construction at stage k: each paradox constructs
    a "problematic" element via a specific operation. -/
```

## Source Excerpt

```lean
def paradox_construction (p : ParadoxWitness) (x k : Nat) : Nat :=
  let pk := primorial k
  if pk == 0 then 0
  else match p with
  | .cantor => (x + 1) % pk         -- diagonal shift (Cantor's d(x) = x+1)
  | .russell => pk - 1 - (x % pk)   -- complement (Russell's ¬x)
  | .goedel => (2 * x) % pk         -- doubling (Gödel numbering)
  | .turing => (x * x + 1) % pk     -- iteration (Turing's step function)
```
