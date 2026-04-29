---
{
  "projection_kind": "taulib_declaration",
  "title": "no_factor_below_of_spec_aux",
  "permalink": "/verify/taulib/docs/book-i-polarity-prime-bridge/no-factor-below-of-spec-aux/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.PrimeBridge`.",
  "declaration_id": "TauLib.BookI.Polarity.PrimeBridge::no_factor_below_of_spec_aux",
  "declaration_slug": "no-factor-below-of-spec-aux",
  "kind": "theorem",
  "name": "no_factor_below_of_spec_aux",
  "module_name": "TauLib.BookI.Polarity.PrimeBridge",
  "module_url": "/verify/taulib/docs/book-i-polarity-prime-bridge/",
  "source_line_start": 76,
  "source_line_end": 102,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimeBridge.lean#L76-L102",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.PrimeBridge",
        "url": "/verify/taulib/docs/book-i-polarity-prime-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimeBridge.lean#L76-L102",
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

- Module: [TauLib.BookI.Polarity.PrimeBridge](/verify/taulib/docs/book-i-polarity-prime-bridge/)
- Source path: [`TauLib/BookI/Polarity/PrimeBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimeBridge.lean#L76-L102)
- Source range: L76-L102
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- ============================================================
-- NO_FACTOR_BELOW: BACKWARD DIRECTION
-- ============================================================
```

## Source Excerpt

```lean
private theorem no_factor_below_of_spec_aux (n : TauIdx) (hn : n ≥ 2) :
    ∀ fuel : Nat, ∀ d : TauIdx, fuel = n - d → d ≥ 2 →
    (∀ k : TauIdx, k ≥ d → k * k ≤ n → n % k ≠ 0) →
    no_factor_below n d = true := by
  intro fuel
  induction fuel using Nat.strongRecOn with
  | _ fuel ih =>
  intro d hfuel hd hspec
  unfold no_factor_below
  split
  · rfl  -- d ≥ n
  · rename_i hdn
    split
    · rfl  -- d * d > n
    · rename_i hdd
      have hle : d * d ≤ n := by simp only [TauIdx] at *; omega
      have hmod : n % d ≠ 0 := hspec d (Nat.le_refl d) hle
      split
      · -- n % d = 0: contradiction with hmod
        rename_i hmod0
        exact absurd hmod0 hmod
      · -- Recurse with d + 1
        have hfuel_lt : n - (d + 1) < fuel := by
          rw [hfuel]; simp only [TauIdx] at *; omega
        exact ih (n - (d + 1)) hfuel_lt (d + 1) rfl
            (by simp only [TauIdx] at *; omega)
            (fun k hk hkk => hspec k (by simp only [TauIdx] at *; omega) hkk)
```
