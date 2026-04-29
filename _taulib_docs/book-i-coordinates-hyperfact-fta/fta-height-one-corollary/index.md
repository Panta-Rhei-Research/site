---
{
  "projection_kind": "taulib_declaration",
  "title": "fta_height_one_corollary",
  "permalink": "/verify/taulib/docs/book-i-coordinates-hyperfact-fta/fta-height-one-corollary/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.HyperfactFTA`.",
  "declaration_id": "TauLib.BookI.Coordinates.HyperfactFTA::fta_height_one_corollary",
  "declaration_slug": "fta-height-one-corollary",
  "kind": "theorem",
  "name": "fta_height_one_corollary",
  "module_name": "TauLib.BookI.Coordinates.HyperfactFTA",
  "module_url": "/verify/taulib/docs/book-i-coordinates-hyperfact-fta/",
  "source_line_start": 103,
  "source_line_end": 112,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactFTA.lean#L103-L112",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.HyperfactFTA",
        "url": "/verify/taulib/docs/book-i-coordinates-hyperfact-fta/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactFTA.lean#L103-L112",
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

- Module: [TauLib.BookI.Coordinates.HyperfactFTA](/verify/taulib/docs/book-i-coordinates-hyperfact-fta/)
- Source path: [`TauLib/BookI/Coordinates/HyperfactFTA.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactFTA.lean#L103-L112)
- Source range: L103-L112
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **FTA-as-height-1 corollary** (Hinge 1, `cor:fta-embedding`):
    when the hyperfactorization of `x` has `C = 1`, it specialises
    to the prime-power factor form `x = a^b · d` where `a ≥ 2` is
    the largest prime divisor (B uniqueness from Wave 6's No-Tie
    Lemma), `b = v_a(x)` is the a-adic valuation, and `d` is the
    a-free remainder.

    Iterated application yields the ordinary FTA factorisation
    `x = p_1^{e_1} · p_2^{e_2} · … · p_k^{e_k}` with
    `p_1 > p_2 > … > p_k`.

    Conversely, the ordinary FTA factorisation determines the ABCD
    chart's `C = 1` specialisation via `B = e_j` and `A = p_j` in
    decreasing order at each recursion stage. -/
```

## Source Excerpt

```lean
theorem fta_height_one_corollary (x a b d : TauIdx)
    (h : ValidABCD x a b 1 d) :
    a ≥ 2 ∧ b ≥ 1 ∧ a ^ b * d = x ∧ (d = 0 ∨ ¬ a ∣ d) :=
  (validABCD_at_height_one_iff x a b d).mp h

-- ============================================================
-- PART 4: Numerical sanity check
-- ============================================================

end Tau.Coordinates
```
