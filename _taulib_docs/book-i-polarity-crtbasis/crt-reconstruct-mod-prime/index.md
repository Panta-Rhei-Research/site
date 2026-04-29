---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_reconstruct_mod_prime",
  "permalink": "/verify/taulib/docs/book-i-polarity-crtbasis/crt-reconstruct-mod-prime/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.CRTBasis`.",
  "declaration_id": "TauLib.BookI.Polarity.CRTBasis::crt_reconstruct_mod_prime",
  "declaration_slug": "crt-reconstruct-mod-prime",
  "kind": "theorem",
  "name": "crt_reconstruct_mod_prime",
  "module_name": "TauLib.BookI.Polarity.CRTBasis",
  "module_url": "/verify/taulib/docs/book-i-polarity-crtbasis/",
  "source_line_start": 467,
  "source_line_end": 475,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L467-L475",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L467-L475",
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
- Source path: [`TauLib/BookI/Polarity/CRTBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L467-L475)
- Source range: L467-L475
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- CRT projection: crt_reconstruct residues k mod p_{l+1} = residues[l] mod p_{l+1}.
    This is the key interface theorem for downstream formal proofs
    (Teichmüller retraction, orthogonality, etc.). -/
```

## Source Excerpt

```lean
theorem crt_reconstruct_mod_prime {k l : TauIdx} (residues : List TauIdx)
    (hl : l < k) (hyp : CRTHyp k) :
    crt_reconstruct residues k % nth_prime (l + 1) =
    residues.getD l 0 % nth_prime (l + 1) := by
  simp only [crt_reconstruct]
  rw [crt_reconstruct_go_mod_prime _ hl hyp 0 k 0 (Nat.zero_le k) (by omega)]
  simp only [Nat.zero_le, ↓reduceIte, Nat.zero_add]

end Tau.Polarity
```
