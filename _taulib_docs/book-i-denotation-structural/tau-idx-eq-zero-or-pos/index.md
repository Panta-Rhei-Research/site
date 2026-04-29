---
{
  "projection_kind": "taulib_declaration",
  "title": "tauIdx_eq_zero_or_pos",
  "permalink": "/verify/taulib/docs/book-i-denotation-structural/tau-idx-eq-zero-or-pos/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Structural`.",
  "declaration_id": "TauLib.BookI.Denotation.Structural::tauIdx_eq_zero_or_pos",
  "declaration_slug": "tau-idx-eq-zero-or-pos",
  "kind": "theorem",
  "name": "tauIdx_eq_zero_or_pos",
  "module_name": "TauLib.BookI.Denotation.Structural",
  "module_url": "/verify/taulib/docs/book-i-denotation-structural/",
  "source_line_start": 387,
  "source_line_end": 390,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L387-L390",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Structural",
        "url": "/verify/taulib/docs/book-i-denotation-structural/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L387-L390",
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

- Module: [TauLib.BookI.Denotation.Structural](/verify/taulib/docs/book-i-denotation-structural/)
- Source path: [`TauLib/BookI/Denotation/Structural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L387-L390)
- Source range: L387-L390
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **τ-native trichotomy for τ-Idx**: every TauIdx is either zero or
    positive.  Delegates to `Nat.eq_zero_or_pos` via the
    `TauIdx := abbrev Nat` definitional alias.

    Wave 38 — Tier 3 nice-to-have from `nat-usage-audit-bookI`.
    Companion to `tauIdx_zero_not_succ` and
    `tauIdx_no_additive_inverse` — closes the trichotomy gap at the
    τ-Idx level so future τ-native code can avoid bare
    `Nat.eq_zero_or_pos` calls. -/
```

## Source Excerpt

```lean
theorem tauIdx_eq_zero_or_pos (n : TauIdx) : n = 0 ∨ n > 0 :=
  Nat.eq_zero_or_pos n

end Tau.Denotation.Structural
```
