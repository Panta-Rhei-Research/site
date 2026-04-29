---
{
  "projection_kind": "taulib_declaration",
  "title": "wave_vs_laplace_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/wave-vs-laplace-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.JReplacesI`.",
  "declaration_id": "TauLib.BookII.Transcendentals.JReplacesI::wave_vs_laplace_check",
  "declaration_slug": "wave-vs-laplace-check",
  "kind": "def",
  "name": "wave_vs_laplace_check",
  "module_name": "TauLib.BookII.Transcendentals.JReplacesI",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/",
  "source_line_start": 116,
  "source_line_end": 123,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/JReplacesI.lean#L116-L123",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.JReplacesI",
        "url": "/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/JReplacesI.lean#L116-L123",
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

- Module: [TauLib.BookII.Transcendentals.JReplacesI](/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/)
- Source path: [`TauLib/BookII/Transcendentals/JReplacesI.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/JReplacesI.lean#L116-L123)
- Source range: L116-L123
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Wave vs Laplace: the two signatures in sector coordinates.
    j^2 = +1: sector product is componentwise (wave eq characteristic coords)
    i^2 = -1: Gaussian product mixes components (elliptic) -/
```

## Source Excerpt

```lean
def wave_vs_laplace_check : Bool :=
  -- Split-complex sector product: componentwise
  let sp1 : SectorPair := to_sectors ⟨2, 3⟩  -- (5, -1)
  let sp2 : SectorPair := to_sectors ⟨1, 4⟩  -- (5, -3)
  let sp_prod := SectorPair.mul sp1 sp2       -- (25, 3)
  -- Verify it equals to_sectors of the split-complex product
  let sc_prod := SplitComplex.mul ⟨2, 3⟩ ⟨1, 4⟩  -- (2*1+3*4, 2*4+3*1) = (14, 11)
  sp_prod == to_sectors sc_prod
```
