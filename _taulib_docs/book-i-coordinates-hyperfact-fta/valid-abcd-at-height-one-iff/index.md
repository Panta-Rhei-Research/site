---
{
  "projection_kind": "taulib_declaration",
  "title": "validABCD_at_height_one_iff",
  "permalink": "/verify/taulib/docs/book-i-coordinates-hyperfact-fta/valid-abcd-at-height-one-iff/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.HyperfactFTA`.",
  "declaration_id": "TauLib.BookI.Coordinates.HyperfactFTA::validABCD_at_height_one_iff",
  "declaration_slug": "valid-abcd-at-height-one-iff",
  "kind": "theorem",
  "name": "validABCD_at_height_one_iff",
  "module_name": "TauLib.BookI.Coordinates.HyperfactFTA",
  "module_url": "/verify/taulib/docs/book-i-coordinates-hyperfact-fta/",
  "source_line_start": 73,
  "source_line_end": 83,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactFTA.lean#L73-L83",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactFTA.lean#L73-L83",
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
- Source path: [`TauLib/BookI/Coordinates/HyperfactFTA.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactFTA.lean#L73-L83)
- Source range: L73-L83
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `ValidABCD x A B 1 D` simplifies to the standard prime-power
    factor form `A ≥ 2 ∧ B ≥ 1 ∧ A^B · D = x ∧ (D = 0 ∨ ¬ A ∣ D)`.
    This is exactly the inductive step of the classical FTA at the
    largest prime divisor `A` of `X`. -/
```

## Source Excerpt

```lean
theorem validABCD_at_height_one_iff (x a b d : TauIdx) :
    ValidABCD x a b 1 d
      ↔ a ≥ 2 ∧ b ≥ 1 ∧ a ^ b * d = x ∧ (d = 0 ∨ ¬ a ∣ d) := by
  unfold ValidABCD
  rw [tower_atom_at_height_one]
  refine ⟨?_, ?_⟩
  · intro ⟨ha, hb, _, h_eq, h_d⟩
    exact ⟨ha, hb, h_eq, h_d⟩
  · intro ⟨ha, hb, h_eq, h_d⟩
    refine ⟨ha, hb, ?_, h_eq, h_d⟩
    exact Nat.one_le_iff_ne_zero.mpr (by decide)
```
