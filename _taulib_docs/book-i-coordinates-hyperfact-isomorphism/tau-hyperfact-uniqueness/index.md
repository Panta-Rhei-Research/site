---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_hyperfact_uniqueness",
  "permalink": "/verify/taulib/docs/book-i-coordinates-hyperfact-isomorphism/tau-hyperfact-uniqueness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.HyperfactIsomorphism`.",
  "declaration_id": "TauLib.BookI.Coordinates.HyperfactIsomorphism::tau_hyperfact_uniqueness",
  "declaration_slug": "tau-hyperfact-uniqueness",
  "kind": "theorem",
  "name": "tau_hyperfact_uniqueness",
  "module_name": "TauLib.BookI.Coordinates.HyperfactIsomorphism",
  "module_url": "/verify/taulib/docs/book-i-coordinates-hyperfact-isomorphism/",
  "source_line_start": 92,
  "source_line_end": 98,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactIsomorphism.lean#L92-L98",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactIsomorphism.lean#L92-L98",
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
- Source path: [`TauLib/BookI/Coordinates/HyperfactIsomorphism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactIsomorphism.lean#L92-L98)
- Source range: L92-L98
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §6 Theorem 7.1 `thm:tau-hyperfact` — uniqueness via
    Wave 6's No-Tie Lemma**.

    For every `x : TauIdx`, `a : TauIdx`, `v : TauIdx`, two
    `IsHyperfactWitness` records agreeing on `(x, a, v)` produce
    the same `(B, C)` components.  This is the structural content
    of paper Theorem 7.1's uniqueness clause, established at the
    Prop level by Wave 6 (I.T56).

    Composing with `hyperfact_D_unique_of_BC` (also Wave 6) gives
    full ABCD uniqueness once (A, v) are pinned. -/
```

## Source Excerpt

```lean
theorem tau_hyperfact_uniqueness (x a v : TauIdx)
    (b c d b' c' d' : TauIdx)
    (h1 : IsHyperfactWitness x a b c d v)
    (h2 : IsHyperfactWitness x a b' c' d' v) :
    b = b' ∧ c = c' := by
  obtain ⟨hc, hb⟩ := hyperfact_BC_unique x a v b c d b' c' d' h1 h2
  exact ⟨hb, hc⟩
```
