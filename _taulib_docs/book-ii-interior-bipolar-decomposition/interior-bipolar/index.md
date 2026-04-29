---
{
  "projection_kind": "taulib_declaration",
  "title": "interior_bipolar",
  "permalink": "/verify/taulib/docs/book-ii-interior-bipolar-decomposition/interior-bipolar/",
  "summary_short": "`def` declaration in `TauLib.BookII.Interior.BipolarDecomposition`.",
  "declaration_id": "TauLib.BookII.Interior.BipolarDecomposition::interior_bipolar",
  "declaration_slug": "interior-bipolar",
  "kind": "def",
  "name": "interior_bipolar",
  "module_name": "TauLib.BookII.Interior.BipolarDecomposition",
  "module_url": "/verify/taulib/docs/book-ii-interior-bipolar-decomposition/",
  "source_line_start": 48,
  "source_line_end": 49,
  "registry_ids": [
    "II.D08"
  ],
  "related_registry_items": [
    {
      "id": "II.D08",
      "title": "Interior Bipolar Decomposition",
      "url": "/registry/object/II.D08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/BipolarDecomposition.lean#L48-L49",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.BipolarDecomposition",
        "url": "/verify/taulib/docs/book-ii-interior-bipolar-decomposition/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/BipolarDecomposition.lean#L48-L49",
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

- Module: [TauLib.BookII.Interior.BipolarDecomposition](/verify/taulib/docs/book-ii-interior-bipolar-decomposition/)
- Source path: [`TauLib/BookII/Interior/BipolarDecomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/BipolarDecomposition.lean#L48-L49)
- Source range: L48-L49
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D08` — Interior Bipolar Decomposition

## Immediate Comment / Docstring

```lean
/-- [II.D08] Interior bipolar decomposition.
    Maps a τ-admissible point to a sector pair (s₊, s₋).
    B-coordinate → e₊-sector, C-coordinate → e₋-sector.

    At finite stages, this is the integer-level shadow of the
    profinite decomposition Ψ_int = e₊ · Ψ(B) + e₋ · Ψ(C). -/
```

## Source Excerpt

```lean
def interior_bipolar (p : TauAdmissiblePoint) : SectorPair :=
  ⟨(p.b : Int), (p.c : Int)⟩
```
