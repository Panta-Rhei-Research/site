---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_roundtrip_formal",
  "permalink": "/verify/taulib/docs/book-i-polarity-crtbasis/crt-roundtrip-formal/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.CRTBasis`.",
  "declaration_id": "TauLib.BookI.Polarity.CRTBasis::crt_roundtrip_formal",
  "declaration_slug": "crt-roundtrip-formal",
  "kind": "theorem",
  "name": "crt_roundtrip_formal",
  "module_name": "TauLib.BookI.Polarity.CRTBasis",
  "module_url": "/verify/taulib/docs/book-i-polarity-crtbasis/",
  "source_line_start": 431,
  "source_line_end": 450,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L431-L450",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.CRTBasis",
        "url": "/verify/taulib/docs/book-i-polarity-crtbasis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L431-L450",
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

- Module: [TauLib.BookI.Polarity.CRTBasis](/verify/taulib/docs/book-i-polarity-crtbasis/)
- Source path: [`TauLib/BookI/Polarity/CRTBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L431-L450)
- Source range: L431-L450
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- CRT round-trip: reconstruct ∘ decompose = id (mod M_k). -/
```

## Source Excerpt

```lean
theorem crt_roundtrip_formal {x k : TauIdx} (hyp : CRTHyp k) :
    crt_reconstruct (crt_decompose x k) k = x % primorial k := by
  -- Strategy: show both sides agree mod each prime, then apply CRT uniqueness.
  have h_agree : ∀ l, l < k →
      crt_reconstruct (crt_decompose x k) k % nth_prime (l + 1) =
      x % nth_prime (l + 1) := by
    intro l hl
    simp only [crt_reconstruct]
    rw [crt_reconstruct_go_mod_prime _ hl hyp 0 k 0 (Nat.zero_le k) (by omega)]
    simp only [Nat.zero_le, ↓reduceIte, Nat.zero_add]
    -- Goal: (crt_decompose x k).getD l 0 % p_{l+1} = x % p_{l+1}
    rw [crt_decompose_getD hl]
    -- Goal: x % p_{l+1} % p_{l+1} = x % p_{l+1}
    exact mod_mod_of_dvd x _ _ ⟨1, (Nat.mul_one _).symm⟩
  -- CRT uniqueness gives agreement mod M_k
  have h_mod := crt_unique_mod hyp h_agree
  -- h_mod : crt_reconstruct ... % M_k = x % M_k
  -- LHS is already < M_k, so % M_k is a no-op
  rw [Nat.mod_eq_of_lt (crt_reconstruct_lt _ (primorial_pos k))] at h_mod
  exact h_mod
```
