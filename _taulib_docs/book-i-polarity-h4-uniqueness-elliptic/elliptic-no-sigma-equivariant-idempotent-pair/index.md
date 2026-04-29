---
{
  "projection_kind": "taulib_declaration",
  "title": "elliptic_no_sigma_equivariant_idempotent_pair",
  "permalink": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/elliptic-no-sigma-equivariant-idempotent-pair/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.H4UniquenessElliptic`.",
  "declaration_id": "TauLib.BookI.Polarity.H4UniquenessElliptic::elliptic_no_sigma_equivariant_idempotent_pair",
  "declaration_slug": "elliptic-no-sigma-equivariant-idempotent-pair",
  "kind": "theorem",
  "name": "elliptic_no_sigma_equivariant_idempotent_pair",
  "module_name": "TauLib.BookI.Polarity.H4UniquenessElliptic",
  "module_url": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/",
  "source_line_start": 276,
  "source_line_end": 284,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L276-L284",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.H4UniquenessElliptic",
        "url": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L276-L284",
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

- Module: [TauLib.BookI.Polarity.H4UniquenessElliptic](/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/)
- Source path: [`TauLib/BookI/Polarity/H4UniquenessElliptic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L276-L284)
- Source range: L276-L284
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §9 elliptic exclusion at integer scale** (the
    Gaussian-multiplication explicit-computation form): for the
    canonical candidate `ξ = i`, the orthogonality requirement on
    `e_± = (1 ± ξ)/2` fails because `(1 + i)(1 - i) = 2 ≠ 0`.

    Compare with the split-complex case: `(1 + j)(1 - j) = 1 - j² =
    1 - 1 = 0` in SplitComplex, which IS the orthogonality
    condition.  The structural difference between `j² = +1`
    (split-complex) and `i² = -1` (elliptic) is exactly what makes
    one admit σ-equivariant idempotents and the other not. -/
```

## Source Excerpt

```lean
theorem elliptic_no_sigma_equivariant_idempotent_pair :
    -- The Gaussian-multiplication witness:
    -- (1+i)(1-i) = 1·1 - 1·(-1) + (1·(-1) + 1·1)i = 1+1 + 0i = 2 ≠ 0
    GaussianElliptic.mul ⟨1, 1⟩ ⟨1, -1⟩ ≠ GaussianElliptic.zero := by
  unfold GaussianElliptic.mul GaussianElliptic.zero
  show (⟨1*1 - 1*(-1), 1*(-1) + 1*1⟩ : GaussianElliptic) ≠ ⟨0, 0⟩
  intro h
  injection h with h_re _
  norm_num at h_re
```
