---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_ring_iso",
  "permalink": "/verify/taulib/docs/book-i-boundary-spectral/spectral-ring-iso/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Spectral`.",
  "declaration_id": "TauLib.BookI.Boundary.Spectral::spectral_ring_iso",
  "declaration_slug": "spectral-ring-iso",
  "kind": "theorem",
  "name": "spectral_ring_iso",
  "module_name": "TauLib.BookI.Boundary.Spectral",
  "module_url": "/verify/taulib/docs/book-i-boundary-spectral/",
  "source_line_start": 123,
  "source_line_end": 134,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Spectral.lean#L123-L134",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Spectral",
        "url": "/verify/taulib/docs/book-i-boundary-spectral/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Spectral.lean#L123-L134",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Boundary.Spectral](/verify/taulib/docs/book-i-boundary-spectral/)
- Source path: [`TauLib/BookI/Boundary/Spectral.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Spectral.lean#L123-L134)
- Source range: L123-L134
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Full ring isomorphism: spectral is a ring homomorphism that is also injective. -/
```

## Source Excerpt

```lean
theorem spectral_ring_iso :
    -- Preserves addition
    (∀ (a b : SplitComplex), spectral (SplitComplex.add a b) =
      SectorPair.add (spectral a) (spectral b)) ∧
    -- Preserves multiplication
    (∀ (a b : SplitComplex), spectral (SplitComplex.mul a b) =
      SectorPair.mul (spectral a) (spectral b)) ∧
    -- Preserves one
    (spectral SplitComplex.one = SectorPair.one) ∧
    -- Injective
    (∀ (a b : SplitComplex), spectral a = spectral b → a = b) :=
  ⟨spectral_add, spectral_mul, spectral_one, spectral_unique⟩
```
