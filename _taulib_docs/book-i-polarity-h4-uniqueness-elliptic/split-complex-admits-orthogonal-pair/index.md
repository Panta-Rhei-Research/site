---
{
  "projection_kind": "taulib_declaration",
  "title": "split_complex_admits_orthogonal_pair",
  "permalink": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/split-complex-admits-orthogonal-pair/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.H4UniquenessElliptic`.",
  "declaration_id": "TauLib.BookI.Polarity.H4UniquenessElliptic::split_complex_admits_orthogonal_pair",
  "declaration_slug": "split-complex-admits-orthogonal-pair",
  "kind": "theorem",
  "name": "split_complex_admits_orthogonal_pair",
  "module_name": "TauLib.BookI.Polarity.H4UniquenessElliptic",
  "module_url": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/",
  "source_line_start": 298,
  "source_line_end": 304,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L298-L304",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L298-L304",
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
- Source path: [`TauLib/BookI/Polarity/H4UniquenessElliptic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L298-L304)
- Source range: L298-L304
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §9 part 5 (split-contrast)**: in SplitComplex, the
    *same* construction `(1 + j)(1 - j)` evaluates to **zero**,
    because `j² = +1` (not `-1` as in the elliptic case).

    This is the structural reason why split-complex admits the
    idempotent pair while Gaussian doesn't: `(1+j)(1-j) = 1 - j² =
    1 - 1 = 0` makes `(1+j)/2 · (1-j)/2 = 0` orthogonality, satisfied;
    while `(1+i)(1-i) = 1 - i² = 1 - (-1) = 2 ≠ 0` fails it. -/
```

## Source Excerpt

```lean
theorem split_complex_admits_orthogonal_pair :
    SplitComplex.mul ⟨1, 1⟩ ⟨1, -1⟩ = SplitComplex.zero := by
  unfold SplitComplex.mul SplitComplex.zero
  -- Split-complex multiplication: (a + bj)(c + dj) = (ac + bd) + (ad + bc)j
  -- (1 + 1j)(1 - 1j) = (1·1 + 1·(-1)) + (1·(-1) + 1·1)j = 0 + 0j
  show (⟨1*1 + 1*(-1), 1*(-1) + 1*1⟩ : SplitComplex) = ⟨0, 0⟩
  simp
```
