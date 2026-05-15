---
{
  "projection_kind": "taulib_declaration",
  "title": "sigmaSwap_on_four_atoms_zero",
  "permalink": "/corpus/taulib/docs/book-i-polarity-h4-boundary-algebra/sigma-swap-on-four-atoms-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.H4BoundaryAlgebra`.",
  "declaration_id": "TauLib.BookI.Polarity.H4BoundaryAlgebra::sigmaSwap_on_four_atoms_zero",
  "declaration_slug": "sigma-swap-on-four-atoms-zero",
  "kind": "theorem",
  "name": "sigmaSwap_on_four_atoms_zero",
  "module_name": "TauLib.BookI.Polarity.H4BoundaryAlgebra",
  "module_url": "/corpus/taulib/docs/book-i-polarity-h4-boundary-algebra/",
  "source_line_start": 215,
  "source_line_end": 218,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L215-L218",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.H4BoundaryAlgebra",
        "url": "/corpus/taulib/docs/book-i-polarity-h4-boundary-algebra/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L215-L218",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Polarity.H4BoundaryAlgebra](/corpus/taulib/docs/book-i-polarity-h4-boundary-algebra/)
- Source path: [`TauLib/BookI/Polarity/H4BoundaryAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L215-L218)
- Source range: L215-L218
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **σ acts on the four atoms by**: 0 ↦ 0, 1 ↦ 1, e_+ ↔ e_-.
    Two fixed atoms (0 and 1) plus one σ-orbit of length 2
    (the {e_+, e_-} pair).  Paper Lemma four-atoms structure. -/
```

## Source Excerpt

```lean
theorem sigmaSwap_on_four_atoms_zero :
    sectorSigma (Truth4.toSectorPair Truth4.F) = Truth4.toSectorPair Truth4.F := by
  show sectorSigma ⟨0, 0⟩ = ⟨0, 0⟩
  rfl
```
