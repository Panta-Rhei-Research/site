---
{
  "projection_kind": "taulib_declaration",
  "title": "cauchyTrace",
  "permalink": "/verify/taulib/docs/book-i-topos-circularity-resolution/cauchy-trace/",
  "summary_short": "`def` declaration in `TauLib.BookI.Topos.CircularityResolution`.",
  "declaration_id": "TauLib.BookI.Topos.CircularityResolution::cauchyTrace",
  "declaration_slug": "cauchy-trace",
  "kind": "def",
  "name": "cauchyTrace",
  "module_name": "TauLib.BookI.Topos.CircularityResolution",
  "module_url": "/verify/taulib/docs/book-i-topos-circularity-resolution/",
  "source_line_start": 422,
  "source_line_end": 435,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L422-L435",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.CircularityResolution",
        "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L422-L435",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookI.Topos.CircularityResolution](/verify/taulib/docs/book-i-topos-circularity-resolution/)
- Source path: [`TauLib/BookI/Topos/CircularityResolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L422-L435)
- Source range: L422-L435
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The Cauchy-iteration trace as a `Nat → Truth4` function — the
    Truth4-side analogue of an `OmegaInverseLimit`-coherent sequence.
    This connects the surface-form §7 stabilisation classification
    to the deep-structural Wave-8 inverse-limit infrastructure: each
    depth `n` carries a truth-value component, and the σ-tail
    equivalence class of the trace is the ω-germ stabilised value.

    NOTE: an `OmegaInverseLimit` is over residues mod primorials and
    so is structurally different from a `Truth4`-valued trace; the
    literal H6.4 inverse-limit appears on the *defect-germ side*
    (a Hinge-3 wave).  On the H6 §7 surface form, the trace shape
    is what matters, and we expose it here for reference. -/
```

## Source Excerpt

```lean
def cauchyTrace (Φ : Truth4 → Truth4) (s : Truth4) : Nat → Truth4 :=
  fun n => cauchyIter Φ n s

/-- The Liar's Cauchy trace from seed `F`: `F, T, F, T, …`. -/
@[simp] theorem cauchyTrace_liar (n : Nat) :
    cauchyTrace liarTemplate F n = (if n % 2 = 0 then F else T) :=
  liar_iter_alternates n

/-- The Truth-teller's Cauchy trace is constant at the seed. -/
@[simp] theorem cauchyTrace_truthTeller (s : Truth4) (n : Nat) :
    cauchyTrace truthTellerTemplate s n = s :=
  truth_teller_constant_at_seed s n

end Tau.Topos
```
