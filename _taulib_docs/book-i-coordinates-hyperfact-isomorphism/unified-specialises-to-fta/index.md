---
{
  "projection_kind": "taulib_declaration",
  "title": "unified_specialises_to_fta",
  "permalink": "/verify/taulib/docs/book-i-coordinates-hyperfact-isomorphism/unified-specialises-to-fta/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.HyperfactIsomorphism`.",
  "declaration_id": "TauLib.BookI.Coordinates.HyperfactIsomorphism::unified_specialises_to_fta",
  "declaration_slug": "unified-specialises-to-fta",
  "kind": "theorem",
  "name": "unified_specialises_to_fta",
  "module_name": "TauLib.BookI.Coordinates.HyperfactIsomorphism",
  "module_url": "/verify/taulib/docs/book-i-coordinates-hyperfact-isomorphism/",
  "source_line_start": 168,
  "source_line_end": 171,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactIsomorphism.lean#L168-L171",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactIsomorphism.lean#L168-L171",
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
- Source path: [`TauLib/BookI/Coordinates/HyperfactIsomorphism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactIsomorphism.lean#L168-L171)
- Source range: L168-L171
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §7.2 Cor 8.2 specialisation to FTA**: the unified
    hyperfactorization theorem at C = 1 specialises to the standard
    FTA prime-power form.

    From Wave's I.T59 (`fta_height_one_corollary`): for any valid
    ABCD with C = 1, the chart reduces to `A^B · D = X` with the
    standard FTA constraints (A ≥ 2, A∤D).  Paper §7.2 says this
    is the height-1 specialisation of the unified theorem. -/
```

## Source Excerpt

```lean
theorem unified_specialises_to_fta (x a b d : TauIdx)
    (h : ValidABCD x a b 1 d) :
    a ≥ 2 ∧ b ≥ 1 ∧ a ^ b * d = x ∧ (d = 0 ∨ ¬ a ∣ d) :=
  fta_height_one_corollary x a b d h
```
