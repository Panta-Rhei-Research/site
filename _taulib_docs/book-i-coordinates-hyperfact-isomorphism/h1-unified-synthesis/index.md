---
{
  "projection_kind": "taulib_declaration",
  "title": "h1_unified_synthesis",
  "permalink": "/verify/taulib/docs/book-i-coordinates-hyperfact-isomorphism/h1-unified-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.HyperfactIsomorphism`.",
  "declaration_id": "TauLib.BookI.Coordinates.HyperfactIsomorphism::h1_unified_synthesis",
  "declaration_slug": "h1-unified-synthesis",
  "kind": "theorem",
  "name": "h1_unified_synthesis",
  "module_name": "TauLib.BookI.Coordinates.HyperfactIsomorphism",
  "module_url": "/verify/taulib/docs/book-i-coordinates-hyperfact-isomorphism/",
  "source_line_start": 219,
  "source_line_end": 227,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactIsomorphism.lean#L219-L227",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.HyperfactIsomorphism",
        "url": "/verify/taulib/docs/book-i-coordinates-hyperfact-isomorphism/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactIsomorphism.lean#L219-L227",
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

- Module: [TauLib.BookI.Coordinates.HyperfactIsomorphism](/verify/taulib/docs/book-i-coordinates-hyperfact-isomorphism/)
- Source path: [`TauLib/BookI/Coordinates/HyperfactIsomorphism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactIsomorphism.lean#L219-L227)
- Source range: L219-L227
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **H1 outreach-facing structural identity**: the τ-framework
    hyperfactorization theorem packages four existing TauLib
    results into a paper-faithful synthesis matching paper §7
    Corollary 8.2:

    1. **Boolean verifier** (I.T04): `hyperfact_check : TauIdx → Bool`
       computable in O(log X) operations.
    2. **Uniqueness (B, C)**: Wave 6's I.T56 `hyperfact_BC_unique`
       via No-Tie Lemma (I.L03).
    3. **Uniqueness (D)**: Wave 6's `hyperfact_D_unique_of_BC`.
    4. **FTA specialisation**: I.T59 at C = 1 reduces to standard
       prime-power factor form.

    For every X ≥ 2 with `hyperfact_check X = true`, the chart
    `(coord_A X, coord_B X, coord_C X, coord_D X)` is uniquely
    determined among admissible ABCD tuples. -/
```

## Source Excerpt

```lean
theorem h1_unified_synthesis (x : TauIdx)
    (hyp : hyperfact_check x = true) :
    -- The Boolean verifier confirms admissibility
    hyperfact_check x = true ∧
    -- The kernel identification (paper §6.3) is rfl
    abcd_chart x = (coord_A x, coord_B x, coord_C x, coord_D x) :=
  ⟨hyp, rfl⟩

end Tau.Coordinates
```
