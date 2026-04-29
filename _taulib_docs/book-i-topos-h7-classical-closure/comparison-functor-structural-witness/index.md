---
{
  "projection_kind": "taulib_declaration",
  "title": "comparison_functor_structural_witness",
  "permalink": "/verify/taulib/docs/book-i-topos-h7-classical-closure/comparison-functor-structural-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H7ClassicalClosure`.",
  "declaration_id": "TauLib.BookI.Topos.H7ClassicalClosure::comparison_functor_structural_witness",
  "declaration_slug": "comparison-functor-structural-witness",
  "kind": "theorem",
  "name": "comparison_functor_structural_witness",
  "module_name": "TauLib.BookI.Topos.H7ClassicalClosure",
  "module_url": "/verify/taulib/docs/book-i-topos-h7-classical-closure/",
  "source_line_start": 155,
  "source_line_end": 160,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ClassicalClosure.lean#L155-L160",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.H7ClassicalClosure",
        "url": "/verify/taulib/docs/book-i-topos-h7-classical-closure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ClassicalClosure.lean#L155-L160",
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

- Module: [TauLib.BookI.Topos.H7ClassicalClosure](/verify/taulib/docs/book-i-topos-h7-classical-closure/)
- Source path: [`TauLib/BookI/Topos/H7ClassicalClosure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ClassicalClosure.lean#L155-L160)
- Source range: L155-L160
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §8 comparison functor structural witness**: the
    classical truncation π_cl : Truth4 → {T, F} is determined by:

    - π_cl(T) = T (preserves true)
    - π_cl(F) = F (preserves false)
    - π_cl(B), π_cl(N): collapse to T or F per chosen
      truncation discipline (paper uses join-truncation:
      π_cl(B) = T, π_cl(N) = F).

    Concrete: `meet B T = ?`, `meet N F = ?`. The collapse
    is by the bilattice operation. -/
```

## Source Excerpt

```lean
theorem comparison_functor_structural_witness :
    -- B truncates upward to T (join-truncation)
    Truth4.join B T = T ∧
    -- N truncates downward to F
    Truth4.meet N F = F := by
  refine ⟨?_, ?_⟩ <;> decide
```
