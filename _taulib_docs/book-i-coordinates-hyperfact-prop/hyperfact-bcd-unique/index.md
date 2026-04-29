---
{
  "projection_kind": "taulib_declaration",
  "title": "hyperfact_BCD_unique",
  "permalink": "/verify/taulib/docs/book-i-coordinates-hyperfact-prop/hyperfact-bcd-unique/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.HyperfactProp`.",
  "declaration_id": "TauLib.BookI.Coordinates.HyperfactProp::hyperfact_BCD_unique",
  "declaration_slug": "hyperfact-bcd-unique",
  "kind": "theorem",
  "name": "hyperfact_BCD_unique",
  "module_name": "TauLib.BookI.Coordinates.HyperfactProp",
  "module_url": "/verify/taulib/docs/book-i-coordinates-hyperfact-prop/",
  "source_line_start": 126,
  "source_line_end": 137,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactProp.lean#L126-L137",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.HyperfactProp",
        "url": "/verify/taulib/docs/book-i-coordinates-hyperfact-prop/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactProp.lean#L126-L137",
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

- Module: [TauLib.BookI.Coordinates.HyperfactProp](/verify/taulib/docs/book-i-coordinates-hyperfact-prop/)
- Source path: [`TauLib/BookI/Coordinates/HyperfactProp.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactProp.lean#L126-L137)
- Source range: L126-L137
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **(B, C, D) uniqueness** for hyperfactorization with fixed A and v:
    composition of `hyperfact_BC_unique` and `hyperfact_D_unique_of_BC`.

    This is the substantive uniqueness content of the Hyperfactorization
    Theorem (orthodox form).  A-uniqueness — that A is forced to be
    the largest prime divisor of x — is the next-wave deliverable. -/
```

## Source Excerpt

```lean
theorem hyperfact_BCD_unique (x a v b₁ c₁ d₁ b₂ c₂ d₂ : TauIdx)
    (h₁ : IsHyperfactWitness x a b₁ c₁ d₁ v)
    (h₂ : IsHyperfactWitness x a b₂ c₂ d₂ v) :
    b₁ = b₂ ∧ c₁ = c₂ ∧ tower_atom a b₁ c₁ * d₁ = tower_atom a b₁ c₁ * d₂ := by
  obtain ⟨h_c, h_b⟩ := hyperfact_BC_unique x a v b₁ c₁ d₁ b₂ c₂ d₂ h₁ h₂
  refine ⟨h_b, h_c, ?_⟩
  -- Substitute b₁ = b₂ and c₁ = c₂ to reuse hyperfact_D_unique_of_BC
  have h₂' : IsHyperfactWitness x a b₁ c₁ d₂ v := by
    rw [h_b, h_c]; exact h₂
  exact hyperfact_D_unique_of_BC x a b₁ c₁ d₁ d₂ v h₁ h₂'

end Tau.Coordinates
```
