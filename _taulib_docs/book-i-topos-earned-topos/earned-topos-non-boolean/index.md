---
{
  "projection_kind": "taulib_declaration",
  "title": "earned_topos_non_boolean",
  "permalink": "/verify/taulib/docs/book-i-topos-earned-topos/earned-topos-non-boolean/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.EarnedTopos`.",
  "declaration_id": "TauLib.BookI.Topos.EarnedTopos::earned_topos_non_boolean",
  "declaration_slug": "earned-topos-non-boolean",
  "kind": "theorem",
  "name": "earned_topos_non_boolean",
  "module_name": "TauLib.BookI.Topos.EarnedTopos",
  "module_url": "/verify/taulib/docs/book-i-topos-earned-topos/",
  "source_line_start": 157,
  "source_line_end": 159,
  "registry_ids": [
    "I.P27"
  ],
  "related_registry_items": [
    {
      "id": "I.P27",
      "title": "Paraconsistent Character",
      "url": "/registry/object/I.P27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L157-L159",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.EarnedTopos",
        "url": "/verify/taulib/docs/book-i-topos-earned-topos/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L157-L159",
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

- Module: [TauLib.BookI.Topos.EarnedTopos](/verify/taulib/docs/book-i-topos-earned-topos/)
- Source path: [`TauLib/BookI/Topos/EarnedTopos.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L157-L159)
- Source range: L157-L159
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P27` — Paraconsistent Character

## Immediate Comment / Docstring

```lean
/-- [I.P27] The earned topos E_τ is non-Boolean.

    A Boolean topos has Ω = {0, 1} (two truth values).
    Our Ω_τ has FOUR truth values (T, F, B, N).
    The complement law ¬¬p = p holds in Boolean topoi
    but fails in E_τ: ¬¬B = ¬N = B, which works,
    but the issue is that B and N are distinct from T and F.

    The explosion barrier (I.T13) gives a direct witness:
    B ⟹ F is not T (it's N), so material implication doesn't
    validate ex falso quodlibet. -/
```

## Source Excerpt

```lean
theorem earned_topos_non_boolean :
    omega_both ≠ omega_true ∧ omega_neither ≠ omega_true := by
  constructor <;> decide
```
