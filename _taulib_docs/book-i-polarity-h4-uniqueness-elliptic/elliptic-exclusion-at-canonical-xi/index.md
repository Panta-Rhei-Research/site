---
{
  "projection_kind": "taulib_declaration",
  "title": "elliptic_exclusion_at_canonical_xi",
  "permalink": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/elliptic-exclusion-at-canonical-xi/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.H4UniquenessElliptic`.",
  "declaration_id": "TauLib.BookI.Polarity.H4UniquenessElliptic::elliptic_exclusion_at_canonical_xi",
  "declaration_slug": "elliptic-exclusion-at-canonical-xi",
  "kind": "theorem",
  "name": "elliptic_exclusion_at_canonical_xi",
  "module_name": "TauLib.BookI.Polarity.H4UniquenessElliptic",
  "module_url": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/",
  "source_line_start": 252,
  "source_line_end": 264,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L252-L264",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L252-L264",
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
- Source path: [`TauLib/BookI/Polarity/H4UniquenessElliptic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L252-L264)
- Source range: L252-L264
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §9 elliptic exclusion concrete witness** (paper Thm
    elliptic-exclusion part 2):

    The canonical candidate σ-anti-fixed element is `ξ = i`, which
    satisfies `σ_ell(i) = -i`.  Building `e_± = (1 ± i)/2` (formally:
    in 2× the units), we get:

      `e_+ · e_- = (1 - i²)/4 = (1 - (-1))/4 = 2/4 = 1/2 ≠ 0`.

    This explicit non-zero result is paper §9's concrete proof that
    Gaussian doesn't admit σ-equivariant orthogonal idempotents.

    **Concrete witness** at the integer-scale (4× scaled to avoid
    halving): `(1+i)·(1-i) = 2`, NOT 0.  Hence the orthogonality
    condition `e_+ · e_- = 0` fails for the canonical candidate. -/
```

## Source Excerpt

```lean
theorem elliptic_exclusion_at_canonical_xi :
    -- (1+i) · (1-i) = 2 ≠ 0 in GaussianElliptic
    GaussianElliptic.mul ⟨1, 1⟩ ⟨1, -1⟩ = ⟨2, 0⟩ ∧
    -- Equivalently: (1+i)·(1-i) ≠ 0
    ⟨2, 0⟩ ≠ (GaussianElliptic.zero) := by
  refine ⟨?_, ?_⟩
  · unfold GaussianElliptic.mul
    show (⟨1*1 - 1*(-1), 1*(-1) + 1*1⟩ : GaussianElliptic) = ⟨2, 0⟩
    simp
  · unfold GaussianElliptic.zero
    intro h
    injection h with h_re _
    norm_num at h_re
```
